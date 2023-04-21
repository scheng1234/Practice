# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 09:17:13 2023

@author: Steven Cheng
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url2 = 'http://py4e-data.dr-chuck.net/comments_1696466.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


wdata = urllib.request.urlopen(url, context=ctx).read()
XMLT = ET.fromstring(wdata)

comments = XMLT.findall('.//comment')
clist = list()

for i in range(len(comments)):
    print(comments[i].find("name").text, comments[i].find("count").text)
    clist.append(int(comments[i].find("count").text))
    
xdata = urllib.request.urlopen(url2, context=ctx).read()
XMLT = ET.fromstring(xdata)

comments = XMLT.findall('.//comment')
dlist = list()

for i in range(len(comments)):
    print(comments[i].find("name").text, comments[i].find("count").text)
    dlist.append(int(comments[i].find("count").text))
    
print(sum(dlist))