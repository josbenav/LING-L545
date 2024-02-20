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
			abbr = token.strip('()')
			if abbr in ['etc.', 'i.e.', 'e.g.', 'v.t.', 'st.', 'cf.', 'fl.']:
				sys.stdout.write(token + ' ')
			elif re.match(r'[a-zA-Z]\.', abbr):
				sys.stdout.write(token + ' ')
			else:
				sys.stdout.write(token + '\n')
		else:
			sys.stdout.write(token + ' ')
	line = sys.stdin.readline()
