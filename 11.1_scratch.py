import re
hand = open('mbox-short.txt')
for line in hand:
	line = line.rstrip()
	if line.find('From: ') >= 0:
		x=re.findall('From:.+@(.+)',line)
		print(x[0])
