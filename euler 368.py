import time
import math
startNum = 0
endNum = 100000000
startint=1
def threeDigitsAlt(number):
    string = str(number)
    length = len(string)
    for i in range (length-2):
        if (string [i] == string[i+1]) and (string [i] == string [i+2]):
            return True
    return False

def threeDigits(number):
    subs = [000,111,222,333,444,555,666,777,888,999]
    string = str(number)
    for sub in subs:
        if str(sub) in string:
            return True
    return False

t = time.clock()
for startint in range( 1,endNum):
    if not threeDigitsAlt(startint):
        startNum = startNum + (1/startint)
t2 = time.clock()
print (time.clock() - t, ' seconds to generate ', endNum, ' iterations')
print (startNum)

    
