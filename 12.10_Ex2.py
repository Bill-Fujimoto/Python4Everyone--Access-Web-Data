#~ Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

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
	#~ print(cmd)
	mysock.send(cmd.encode())
	char_count = 0
	while True:
		data = mysock.recv(1000).decode()
		if (len(data) < 1):
			break
		else:
			char_count += len(data)
		if char_count <= 4000:
			print(data,end='')
				
mysock.close()
print()
print(char_count)
print("done")


