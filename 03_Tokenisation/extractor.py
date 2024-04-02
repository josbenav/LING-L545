import sys

lines = sys.stdin.readlines()


"""#step(0)
#reading the zh_pud-ud-test.conllu file
for line in lines:
        print(line)"""

"""##creating file one
#step(1)
#extracting sentences from the zh_pud-ud-test.conllu file
sentences = []
for line in lines:
        words = line.split()
        if len(words) > 0:
                if words[1] == 'text':
                        string = ' '.join(words[3:])
                        sentences.append(string)

#printing all the sentences in one string
# print(sentences)
#printing sentences in individual lines
# for elements in sentences: 
#         print(elements)

#step(2)
#writing the original.txt file
with open('original.txt', 'w') as f:
        for elements in sentences:
                f.write(elements +'\n')"""

"""##creating file two
#step(3)
#tokenizing the sentences from the zh_pud-ud-test.conllu file
sentences = []
token = []
for line in lines:
        words = line.split()
        if len(words) > 0:
                if words[0].isnumeric():
                        token.append(words[2])
        else:   
                sentences.append(token)
                token = []

#printing tokenized elements in one string
# print(sentences)  
#printing tokenized elements in individual strings
for elements in sentences: 
        print(elements)

#step(4)
#creating the tokenized.txt file
with open('tokenized.txt', 'w') as f:
        for elements in sentences:
                f.write(' '.join(elements)+'\n')"""

#after creating file one and two
#split the files (in terminal using wc -l)
#head -n 800 original.txt > original.train.txt 
#tail -n 200 original.txt > original.test.txt 
#head -n 800 tokenized.txt > tokenized.train.txt
#tail -n 200 tokenized.txt > tokenized.test.txt

##creating file three
#step(5)
#creating a dictionary.txt file
wordlist = []   
for line in lines:
        words = line.split()
        for word in words:
                wordlist.append(word)

#printing the list of dictionary items
#cat tokenized.train.txt | python3 extractor.py  
for element in wordlist:
        print(element)

#step(6)
#creating the dictionary.txt file from the tokenized.train.txt
with open('dictionary.txt', 'w') as f:
        for word in set(wordlist):
                f.write(word + '\n')
