# coding UTF-8

import urllib.request
from bs4 import BeautifulSoup
import re

url = 'http://medical.itp.ne.jp/byouki/md-kodomo/sm-shinseiji/'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
names = list(map(lambda x: re.split('[(<{＜（]' ,x.string)[0] ,soup.select('.equalHeight .sName a')[1:]))
print(names)
