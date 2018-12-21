#~ Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. Don't worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request, urllib.parse, urllib.error
#~ from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')

try:
	html = urllib.request.urlopen(url, context=ctx).read()
	lines = html.decode().splitlines()
except urllib.error.HTTPError as error:
	print('URL caused HTTP error')
except urllib.error.URLError as error:
	print('URL improperly formatted')
except UnicodeDecodeError as error:
	print("UTF-8 codec can't decode")
else:
	char_count = 0
	for line in lines:
		#~ print(line)
		char_count += len(line)
		if char_count <= 4000:
			print(line)
	print()
	print(char_count)
	
print("done")


