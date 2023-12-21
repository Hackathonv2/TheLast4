


import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
dict = {}

for line in lines[1:]:
	for word in line.split(' '):
		if word in dict:
			dict[word] += 1
		else:
			dict[word] = 1
print(len(dict))