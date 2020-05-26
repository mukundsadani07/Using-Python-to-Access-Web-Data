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

count = int(input("Enter count:"))
position = int(input("Enter position:"))-1
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

order=[]
# Retrieve all of the anchor tags
tags = soup('a')
for i in range(count):
        link = tags[position].get('href', None)
        print("Retrieving:",link)
        order.append(tags[position].contents[0])
        html = urllib.request.urlopen(link, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        link = tags[position].get('href', None)
print(order[-1])
