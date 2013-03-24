import time
import math
def right(number):
    if number == 1:
        return True
    elif number == 89:
        return True
    else:
        return False
    
def chain(number):
    answer = number
    while not right(answer):
        string = str(answer)
        total=0
        for char in string:
            total = total + (int(char)**2)
        answer= total
    return answer


start = time.clock()
highloops = [2,3,4]
lowloops = [1]
top = 10000000
high = highloops.append
low = lowloops.append
log = math.log10
for i in range (5,top):
    if chain(i)==1:
        low(i)
    else:
        high(i)
    if log(i)==int(log(i)):
        print(i,' numbers took ,',  time.clock()-start, ' seconds, and found', len(highloops))

elapsed = (time.clock() - start)
print (len(highloops))
print (elapsed, ' seconds')
