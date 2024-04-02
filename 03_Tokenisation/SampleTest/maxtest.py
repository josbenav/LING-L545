import sys

# dictionary = open('max.dict.sample.test.txt', 'r')
# sentences = open('max.orig.sample.test.txt', 'r')

for sentence in open('max.orig.sample.test.txt', 'r'):

# for sentence in sys.stdin.readlines():

# strip_sent = sentence.rstrip('\n')

    def MAXMATCH(sentence, dictionary):
        if not sentence:
            return []
        for i in range(len(sentence), 0, -1):
        # for i in range(len(sentence) -1, -1, -1):
            firstword = sentence[:i+1]
            remainder = sentence[i+1:len(sentence)]
            if firstword in dictionary:
                return [firstword] + MAXMATCH(remainder, dictionary)

    # if no word is found, make one-character word
        firstword = sentence[0]
        remainder = sentence[1:len(sentence)]
        return [firstword] + MAXMATCH(remainder, dictionary)

    with open('max.dict.sample.test.txt', 'r') as file:
        match_element = [line.strip() for line in file]
        maxmatch_result = MAXMATCH(sentence.rstrip('\n'), match_element)
        print(' '.join(maxmatch_result))
