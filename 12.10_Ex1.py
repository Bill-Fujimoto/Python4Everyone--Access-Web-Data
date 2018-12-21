#Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.

import socket

url = input('Enter url: ')
url_split = url.split('/')

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	mysock.connect((url_split[2], 80))

except:
	print('URL Host improperly formatted')
    
else:
	cmd = 'GET '+url+' HTTP/1.0\r\n\r\n'
	#~ cmd = item.encode()
	mysock.send(cmd.encode())
	
	while True:
	    data = mysock.recv(512)
	    if (len(data) < 1):
	        break
	    print(data.decode(),end='')
		
mysock.close()
print("done")

#~ http://py4e-data.dr-chuck.net/known_by_Fikret.html
