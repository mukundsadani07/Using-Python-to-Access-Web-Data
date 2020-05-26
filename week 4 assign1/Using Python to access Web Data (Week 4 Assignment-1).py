from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
total = 0
count = 0
# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    w = tag.contents[0]
    total = total +int(w)
    count = count + 1
print("count",count)
print("sum", total)
