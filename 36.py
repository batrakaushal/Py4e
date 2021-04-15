import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print(data)
print('Retrieved', len(data), 'characters')
info = json.loads(data)
#print(info)
total=0
for items in info["comments"]:
    #print(items["count"])
    s=int(items["count"])
    #print(s)
    total=total+s
print(total)
