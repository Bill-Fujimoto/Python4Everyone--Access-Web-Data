fname = input('Enter the file name: ')
try:
	fhand = open(fname, "r")
except:
	print('File cannot be opened:', fname)
	exit()
	
mail_count = {}	
for line in fhand:
	if line.startswith('From:'):
		line = line.split()
		for word in line:
			if "@" in word:
				#print(word)
				if word not in mail_count:
					mail_count[word] = 1
				else:
					mail_count[word] += 1

print(mail_count)
print()
fhand.close()	

largest = None
for name in mail_count:
	if largest == None or mail_count[name] > largest:
		largest = mail_count[name]
		email = name
		
print(email, largest)
