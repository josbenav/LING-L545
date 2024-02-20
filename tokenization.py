import sys, re 


abbr = ['etc.', 'i.e.', 'e.g.', 'v.t.', 'st.', 'cf.', 'fl.']

def tokenise(line, abbr):
	line =  re.sub(r'([\(\)"?:!;])', r' \g<1> ', line)
	line =  re.sub(r'([^0-9]),', r'\g<1> ,', line)
	line =  re.sub(r',([^0-9])', r', \g<1>', line)
	line =  re.sub(r'  *', r' ', line)

	tokens = []
	for token in line.strip().split(' '):
		if token == '':
			continue
		if token[-1] == '.' and token not in abbr:
			token = token[:-1] + ' .'
		tokens.append(token)

	return tokens

line = sys.stdin.readline()
while line: 
	tokens = tokenise(line, abbr)
	print(' '.join(tokens))
	line = sys.stdin.readline()
