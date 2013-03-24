import math
trilist = []
for n in range (1000):
    t=n*(n+1)/2
    trilist.append(t)

def triTest(t):
    if t in trilist:
        return True
    else:
        return False
        
def findVal(word):
    total = 0
    for char in word:
        total = total + ord(char)-64
    return (total)
words = open('/usr/share/dict/web2').read()
wordlist = words.split('/n')

triwords = []
for word in wordlist:
    if triTest(findVal(word)):
        triwords.append(word)
for word in triwords:
    print (word, " ", findVal(word))
print (len(triwords))
