import math
import time
def primetest(number):
    answer = True
    for i in range (2,math.floor(math.sqrt(number))+1):
        if (number % i) == 0:
            answer= False
    return answer
def removeUnlikelys(primelist):
    removelist = ['0','2','4','5','6','8']
    for i in primelist:
        string = str (i)
        for item in removelist:
            if item in string:
                primelist.remove (i)
    return primelist
def rotate (number):
    string = str(number)
    string.append(string[0])
    string=string[1::]
    return int(string)
testnumber = 123456789
for i in range (10):
    for i in range (len(str(testnumber))):
        testnumber= rotate (testnumber)
        print (testnumber)
start = time.clock()
primelist = []
for i in range (2,100):
    if primetest(i):
        primelist.append(i)
print (primelist)
print (time.clock() - start, ' seconds via individual loop')
removeUnlikelys(primelist)
print (time.clock() - start, ' seconds remove unlikelies')
primelist.append(2)
primelist.append(5)
print (time.clock() - start, ' seconds add two back')
primelist.sort()
print (primelist)
print (time.clock() - start, ' seconds after sort')
for number in primelist:
    testnumber = number
    for i in range (len(str(number))):
        testnumber= rotate (testnumber)
        if not primetest(testnumber):
            primetest.remove(number)
            break
print (primelist)
print (time.clock() - start, ' seconds after removal')
