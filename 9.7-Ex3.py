fname = input('Enter the file name: ')
try:
	fhand = open(fname, "r")
except:
	print('File cannot be opened:', fname)
	exit()
	
count = {}	
for line in fhand:
	if line.startswith('From:'):
		line = line.split()
		for word in line:
			if "@" in word:
				print(word)
				if word not in count:
					count[word] = 1
				else:
					count[word] += 1

print(count)
fhand.close()	
