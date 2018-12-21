# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero
import re
hand = open('mbox.txt')
total=0
count=0
for line in hand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9.]+)', line)
    if len(x) > 0:
        total += int(x[0])
        count += 1

print(total/count)
