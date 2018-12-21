fname = input('Enter the file name: ')
try:
	fhand = open(fname, "r")
except:
	print('File cannot be opened:', fname)
	exit()
	
count = {}	
for line in fhand:
	if line.startswith('From'):
		line = line.split()
		if len(line) > 2:
			if line[2] not in count:
				count[line[2]] = 1
			else:
				count[line[2]] += 1
print(count)
fhand.close()	
