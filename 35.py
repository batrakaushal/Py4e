import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
data=data.decode()
tree = ET.fromstring(data)

results = tree.findall('.//count')
print(len(results))
score=[]
count=0
for i in results:
    score=i.text
    score=int(score)
    #print(score)
    count=count+score
print(count)
