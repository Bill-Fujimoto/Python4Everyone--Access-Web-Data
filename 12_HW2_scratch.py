# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
#~ index = int(input('Enter url position: '))
cycles = int(input('Enter cycle count: '))

loop = 1
while loop <= cycles:
	
	html = urllib.request.urlopen(url, context=ctx).read()
	#~ soup = BeautifulSoup(html, 'html.parser')
	print(html)
	#~ # Retrieve all of the anchor tags
	#~ tags = soup('a')
	#~ url = tags[index -1].get('href', None)
	loop += 1
	
#~ print(tags[index -1].contents[0])
