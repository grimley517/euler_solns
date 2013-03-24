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
while number<2000000:
    if isprime(number):
        primelist.append(number)
        if len(primelist)%100 ==0:
            print ('primelist has {length} members the highest of which is {highest}' .format(length = len(primelist), highest = primelist[len(primelist)-1]))
    number = number +1
total = 0
for prime in primelist:
    total = total + prime
print (total)
    
