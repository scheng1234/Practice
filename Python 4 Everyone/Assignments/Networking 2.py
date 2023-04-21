# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = "https://py4e-data.dr-chuck.net/comments_42.html"
    
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')

htmlc = list()
for tag in tags:
    # Look at the parts of a tag
##    print('TAG:', tag)
##    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
##    print('Attrs:', tag.attrs)

    htmlc.append(tag.contents[0])

htmlc = [int(x) for x in htmlc]
