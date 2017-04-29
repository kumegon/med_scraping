# coding UTF-8

import urllib.request
from bs4 import BeautifulSoup
import re
from functools import reduce
import csv


url = 'http://www.medo.jp/b.htm'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

#print(soup.select('html')[0].string)

regex = r'【.*】'
content = list(map(lambda x: x, re.findall(regex, soup.get_text())))
print(content)

with open('desease4.csv', 'a') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    for i in content:
      writer.writerow([i])     # list（1次元配列）の場合
