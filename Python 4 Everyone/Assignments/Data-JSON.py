"""
Created on Fri Feb 20 00:11:08 2023

@author: Steven Cheng
"""



import urllib.request, urllib.parse, urllib.error
import json
import ssl

url = input('Enter - ')
if len(url) < 1:
    url = "https://py4e-data.dr-chuck.net/comments_42.json"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(url, context=ctx).read()
jdata = json.loads(data)

lst = list()
for i in jdata['comments']:
    lst.append(int(i['count']))

print(sum(lst))
