"""
Created on Fri Feb 20 00:11:08 2023

@author: Steven Cheng
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = "https://py4e-data.dr-chuck.net/known_by_Fikret.html"

elif re.search("html", url) == None:
    url = eval(url)

    
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
##for tag in tags:
##    print(tag.get('href', None))

link = tags[17].get('href')

print(link)







