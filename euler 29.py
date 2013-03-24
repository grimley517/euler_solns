import cProfile
import math
import time
start=time.clock()
intlist = []
power=math.pow
append=intlist.append
count = intlist.count
for a in range(2,101):
    for b in range(2,101):
         number = power(a,b)
         if count(number)==0:
             append(number)

print (len(intlist))
print (time.clock()-start)

