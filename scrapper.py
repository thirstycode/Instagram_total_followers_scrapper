# <--- importing neccessary modules----->
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from datetime import datetime as dt
from config import usernames
import pandas
soup_list = []

# TO DO
# <--- find an alternative to execute client side js to load all the web page without using selenium (in background as requests)----->
# Note : Script is working fine with selenium


# <---Selenium Driver----->
driver = webdriver.Chrome(executable_path = "assets" + "\\" + "chromedriver.exe")

for loop in usernames:
    url = "https://www.instagram.com/" + loop
    # opening the page to execute js
    driver.get(url)
    # saving page_source in soup
    soup = bs(driver.page_source,"html.parser")
    soup_list.append(soup)
# <--- Closing The Selenium Driver---->
driver.quit()

new_column = []
for soupnew in soup_list:
    # finding the total followers element
    testing = soupnew.find_all('span',{'class':'_fd86t'})
    testing1=[testing[1]]
    for title in testing1:
        tile_text = title.get('title')
        new_column.append(tile_text)
# <--- Opening export.csv ----->
file = pandas.read_csv("export.csv")
t= dt.now()
# deleting first column
file.drop(file.columns[[0]], axis=1, inplace=True)
# adding column to export.csv with time
file[t.strftime('%I:%M %p %d-%m')]=new_column
# rewriting export.csv
file.to_csv("export.csv")
