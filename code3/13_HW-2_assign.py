import json
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#~ url = input('Enter url: ')
url = 'http://py4e-data.dr-chuck.net/comments_81462.json'
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

# convert dictionary-like string to dict object
info = json.loads(data)

#remove 'note' element from dictionary
#~ info.pop('note')

total = 0
for item in info['comments']:
    print('Name:', item['name'])
    print('Count:', item['count'])
    total += int(item['count'])

print(total)
