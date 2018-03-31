# Instagram_total_followers_scrapper
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)
[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
<br>
<br>
**Crawls Total Followers From List Of Instagram Usernames And Exports It To Csv File With DateTime Details**
<br>
### Installation:

```bash
1. pip install -r requirements.txt
```
2. Download ```chromedriver``` for your system [from here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Extract the .zip file and put it in ```/assets``` folder.
3. Edit ```config.py``` to add usernames in it. Also Make Sure That ```Export.csv``` has usernames to be same as in ```config.py``` or else there will be error from Pandas.

#### Execute It:
```bash
1. python scrapper.py
```
<br>
Instagram Usually Doesnt Display All Exact Number OF Followers If The Account Has More Than 10,000 Followers. This Script Makes Your Work Easy And Helps To Keep A Track On Your Followers In Instagram Account
<br>
