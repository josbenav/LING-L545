import sys
import re
import string
import unicodedata
from collections import Counter

text = sys.stdin.readlines()
validchr = "aeiouáéíóúbcdfghijklmnñpqrstvwxyz"
numbers = "1234567890"
counts = Counter()

ok_char = set(validchr + validchr.upper() + ' \n' + string.punctuation + numbers)

for line in text:
        if set(line) < ok_char:
                sys.stdout.write(line)
        else:
                counts.update([c for c in line if c not in ok_char])

for char, total in counts.most_common():
        if char not in ok_char:
                print('%d\t%s\t%x\t%a' % (total, char, ord(char), unicodedata.category(char)), file=sys.stderr)
"""
for char, total in counts.most_common():
        category = unicodedata.category(char)
        if (char not in ok_char) and (category.startswith('Zs') or category.startswith('Cf')):
                char = unicodedata.normalize('NFKC', char)
        print('%d\t%s\t%x' % (total, char, ord(char)), file=sys.stderr)
"""
