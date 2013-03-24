import math
numberlist = []
top = 2000000
for i in range (2,top):
    numberlist.append(i)
print (len(numberlist))
for number in numberlist:
    if number < math.sqrt(top):
        for i in range (number,int(top/number)):
            nonprime = i*number
            if numberlist.count(nonprime)!=0:
                numberlist.remove(nonprime)
        print('After {0}s removed, there are {1} members'.format(number, len(numberlist)))    
total = 0
for number in numberlist:
    total = total + number
print (total)
