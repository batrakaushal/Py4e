# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count=input('Enter count: ')
position=input('Enter position: ')
position=float(position)
count=float(count)

# Retrieve all of the anchor tags
tags = soup('a')
i=0
for tag in tags:
    i=i+1
    if i==position:
        print('URL:', tag.get('href', None))
        html = urllib.request.urlopen(tag.get('href', None), context=ctx).read()
        j=0
        while j!=count-1:
            j=j+1
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            i=0
            for tag in tags:
                i=i+1
                if i==position:
                    print('URL:', tag.get('href', None))
                    html = urllib.request.urlopen(tag.get('href', None), context=ctx).read()
                    continue

    else:
        continue
