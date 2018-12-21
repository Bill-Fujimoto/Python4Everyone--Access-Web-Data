import re
regex = open('regex_sum_81457.txt')
total=0
values=0
lines=0
for line in regex:
	lines += 1
	line = line.rstrip()
	num_list = re.findall('([0-9]+)', line)
	print(num_list)
	if len(num_list) > 0:
		values += len(num_list)
		for num in num_list:
			total += int(num)
        
print(total, values, lines)
