# coding UTF-8

import urllib.request
from bs4 import BeautifulSoup
import re
from functools import reduce
import csv


url = 'http://www.weblio.jp/ontology/%E7%97%85%E6%B0%97%E3%83%BB%E3%81%91%E3%81%8C_1'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

content = []
names = [re.split('[(<{＜（［]' ,x.get('title'))[0] for x in soup.select('.subCatWordsB a') if x.string]
print(names)
content.append(names)

with open('desease3.csv', 'a') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    for i in content:
      for j in i:
        print(j)
        writer.writerow([j])     # list（1次元配列）の場合
      writer.writerow('')
