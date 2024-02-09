import sys
import re

#line = sys.stdin.readline()

#while line:
#	line = line.strip()
#	for c in '!?.':
#		line = line.replace(c, c + '\n')
#	sys.stdout.write(line)
line = sys.stdin.readline()

while line:
	for token in line.strip().split(' '):
		if not token:
			continue
		if token [-1] in '!?':
			sys.stdout.write(token + '\n')
		elif token[-1] == '.':

			if token in ['a. C.', 'd. C.', 'J.', 'etc.', 'i.e.', '(e.g.']:
				sys.stdout.write(token + ' ')
			elif re.match('[a-zA-Z]\.', token):
				sys.stdout.write(token + ' ')
			else:
				sys.stdout.write(token + '\n')
		else:
			sys.stdout.write(token + ' ')
	line = sys.stdin.readline()
