import sys
import re
import string
from collections import Counter

text = sys.stdin.readlines()
validchr = "aeiouáéíóúbcdfghijklmnñpqrstvwxyz"
numbers = "01234567890"
counts = Counter()

characters = set(validchr + validchr.upper() + ' \n' + string.punctuation + numbers)

for line in text:
        if set(line) < characters:
                sys.stdout.write(line)
        else:
                counts.update(line)

for char, total in counts.most_common():
        if char not in characters:
                print(total, '\t', char, file=sys.stderr)
