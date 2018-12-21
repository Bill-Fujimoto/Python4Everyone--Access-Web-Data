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
fhand.close()
#print(mail_count)
#print()
	

lst=[]
for name,count in mail_count.items():
	lst.append((count,name))
lst.sort(reverse=True)
#print(lst)
#print()
#print(max(lst)[1],max(lst)[0])		
print(lst[0][1],lst[0][0])
