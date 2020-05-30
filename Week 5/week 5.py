import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url= input("Enter location:")
print("Retrieving",url)

data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
count = 0
total = 0
for comments in tree.findall('comments/comment'):
    total += int(comments.find('count').text)
    count = count + 1
print("count:",count)
print("Sum:",total)



