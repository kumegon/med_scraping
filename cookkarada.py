# coding UTF-8

import urllib.request
from bs4 import BeautifulSoup
import re
from functools import reduce
import csv


url = 'https://www.cocokarada.jp/disease/'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
urls = list(map(lambda x: x.get('href'), soup.select('li.medium a')))

content = []
print(urls)
for url in urls:
  content_url = 'https://www.cocokarada.jp/' + str(url)
  html = urllib.request.urlopen(content_url)
  soup = BeautifulSoup(html, "html.parser")
  names = [re.split('[(<{＜（［]' ,x.string)[0] for x in soup.select('#disease-list .noarrow a') if x.string]
  print(names)
  content.append(names)

with open('desease2.csv', 'a') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    for i in content:
      for j in i:
        print(j)
        writer.writerow([j])     # list（1次元配列）の場合
      writer.writerow('')
