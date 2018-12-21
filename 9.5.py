fname = input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print('File cannot be opened:', fname)
	exit()

import string
string.punctuation

counts = {}
for line in fhand:
	line = line.rstrip()
	line = line.translate(line.maketrans('','',string.punctuation))
	line = line.lower()
	words = line.split()
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word]+= 1

print(counts)
#print()
#print(counts.keys())

