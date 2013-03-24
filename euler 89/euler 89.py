romanDict =({'I':1,'V':5,'X':10,'L':50, 'C':100,'D':500,'M':1000}) 
def evaluate(rnumber):
    number=0
    for letter in rnumber:
        number = number + romanDict.get(letter,0)
    return number

def removePairs(rnumber):
    if 'IV' in rnumber:
       rnumber= rnumber.replace('IV','IIII')
    if 'IX' in rnumber:
        rnumber = rnumber.replace('IX','VIIII')
    if 'XL' in rnumber:
        rnumber= rnumber.replace('XL','XXXX')
    if 'XC' in rnumber:
        rnumber= rnumber.replace('XC','LXXXX')
    if 'CD' in rnumber:
       rnumber= rnumber.replace('CD','CCCC')
    if 'CM' in rnumber:
        rnumber=rnumber.replace('CM','DCCCC')
    return rnumber

def addPairs(rnumber):
    if 'VIIII' in rnumber:
        rnumber=rnumber.replace('VIIII','IX')
    if 'IIII' in rnumber:
        rnumber=rnumber.replace('IIII','IV')
    if 'LXXXX' in rnumber:
        rnumber=rnumber.replace('LXXXX','XC')
    if 'XXXX' in rnumber:
        rnumber=rnumber.replace('XXXX','XL')
    if 'DCCCC' in rnumber:
        rnumber=rnumber.replace('DCCCC','CM')
    if 'CCCC' in rnumber:
        rnumber=rnumber.replace('CCCC','CD')
    return rnumber        

def romanise(number):
    letters = sorted(romanDict, key = romanDict.get, reverse=True)
    answer = ''
    for i in letters:
        while number >= romanDict.get(i):
            answer = answer +i
            number=number-romanDict.get(i)
    return answer
    


number = open ('roman.txt', mode = 'rt',buffering = 1)
origLength = 0
for line in number:
    line = line.lstrip()
    line=line.rstrip()
    origLength += len(line)
print (origLength)

print(sorted(romanDict, key = romanDict.get, reverse=True))

number = open ('roman.txt', mode = 'rt',buffering = 1)
outfile = open('romanout.txt', mode = 'wt', buffering = 1)
for line in number:
    num = evaluate(removePairs(line))
    ans = romanise(num)
    ans = addPairs(ans)
    print (ans , end = '\n', file=outfile)

number= open('romanout.txt', mode = 'rt', buffering = 1)
newLength =0
for line in number:
    line=line.lstrip()
    line=line.rstrip()
    newLength += len(line)
print (newLength)
print (origLength - newLength)
