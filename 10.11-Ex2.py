fname = input('Enter the file name: ')
try:
	fhand = open(fname, "r")
except:
	print('File cannot be opened:', fname)
	exit()
##### This counts the number of occurences of each hour in the "From"#####	
hour_count = {}	
for line in fhand:
	if line.startswith('From '):
		line = line.split()
		#print(line)
		if len(line) > 5:
			time = line[5].split(":")
			#print(time)
			if time[0] not in hour_count:
				hour_count[time[0]] = 1
			else:
				hour_count[time[0]] += 1
fhand.close()

##### This arranges the hour_count dictionary into list of tuples which is
#then sorted by the hour value (dict can't be sorted apparently) ####

most_hours=[]
for hour, count in hour_count.items(): #.items() returns a list of tuples from dict.
	most_hours.append((hour, count)) # .append adds only 1 element ((tuple)) to list
	
most_hours.sort()  # sorts list of tuples based on first element in tuple
for hour, count in most_hours:
	print(hour, count)



