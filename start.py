# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 10:54:21 2017

@author: Kunal

Modified on Tue Nov 7 02:20:59 2017
Modified by Krishna

Modified again by Kunal *wink* *wink*
"""

import bs4
from GUIController import display
from urllib.request import urlopen

testpage = 'http://kgec.edu.in/notice/Administrative/'
html = urlopen(testpage)
soup = bs4.BeautifulSoup(html, 'html.parser')

data = []
table = soup.find('table', attrs={'class': 'table table-hover'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])  # Get rid of empty values

notices = []

for lists in data:
    notices.append(lists[4] + '\n')

readfile = open("Text3.txt", "r")  # creating a file handle to read

linesread = readfile.readlines()

temp3 = [item for item in notices if item not in linesread]

writefile = open("Text3.txt", "w")

for j in notices:
    writefile.write(j)

if len(temp3) != 0:
    for item in temp3:
        display(txt=item)
        # toaster.show_toast(item,icon_path="/download.jpg",duration=10)



