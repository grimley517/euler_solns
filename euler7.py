primelist = [2,3,5,7]
def isprime (number):
    result = True
    global primelist
    for prime in primelist:
        if number % prime ==0:
            result = False
            break
    return result
number = 8
while len(primelist)<10002:
    if isprime(number):
        primelist.append(number)
        print ('primelist has {length} members' .format(length = len(primelist)))
    number = number +1
print (primelist[10000])
    
