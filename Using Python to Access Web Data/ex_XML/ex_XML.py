import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
sumtotal = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
xml = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)
for numbers in tree.findall(".//count"):
    sumtotal = sumtotal + int(numbers.text)
print(sumtotal)
