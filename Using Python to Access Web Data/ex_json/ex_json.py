import urllib.request, urllib.parse, urllib.error
import ssl
import json
sumtotal = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
data = urllib.request.urlopen(url, context=ctx).read().decode()

try:
     info = json.loads(data)
except:
    info = None

print(json.dumps(info, indent=4))

for item in info["comments"]:
    sumtotal = sumtotal + int(item["count"])
print(sumtotal)
