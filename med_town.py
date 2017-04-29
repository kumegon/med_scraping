# coding UTF-8

import urllib.request
from bs4 import BeautifulSoup
import re
from functools import reduce
import csv

def delete_col(urls):
  result = []
  for url in urls:
    if url.string != 'コラム':
      result.append(url)
  return list(map(lambda x: x.get('href'), result))
url = 'http://medical.itp.ne.jp/byouki/'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
urls = delete_col(reduce(lambda x,y: x+y,list(map(lambda x: x.find_all('a')[1:], soup.select('.searchSickBox.section02 .section02.smtp ul.listType01.colTwo.equalHeight')))))

content = []

for url in urls:
  content_url = 'http://medical.itp.ne.jp/' + str(url)
  html = urllib.request.urlopen(content_url)
  soup = BeautifulSoup(html, "html.parser")
  names = [re.split('[(<{＜（]' ,x.string)[0] for x in soup.select('.resultsList .equalHeight .sName a')[1:] if x.string]
  print(names)
  content.append(names)

with open('desease.csv', 'a') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    for i in content:
      for j in i:
        print(j)
        writer.writerow([j])     # list（1次元配列）の場合
