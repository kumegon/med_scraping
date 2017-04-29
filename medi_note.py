# coding UTF-8

import urllib.request
import re
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = 'https://medicalnote.jp/diseases'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get(url)
sleep(2)
print(1)
links = list(map(lambda x: x.text,browser.find_elements_by_xpath("//a[contains(@class,'ng-binding')]")))
print(links)
content = []
names = [re.split('[(<{＜（［]' ,x)[0] for x in links if x]
content.append(names)

with open('desease5.csv', 'a') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    for i in content:
      for j in i:
        writer.writerow([j])     # list（1次元配列）の場合
