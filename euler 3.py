import math

def isprime(numbe):
    prime = True
    for i in range (2, int(math.sqrt(numbe))):
        if numbe % i ==0:
            prime = False
    return prime

def iscomposite (numbe):
    result = not isprime(numbe)
    return result

number = 600851475143
factors = [1]
for i in range (1, int(math.sqrt(number))):
    if number % i == 0:
        print (i, ' is a factor')
        factors.append(i)  
primefactors = []
for factor in factors:
    if isprime (factor):
        print (factor, ' is a prime factor')
        primefactors.append(factor)
primefactors.sort(reverse=True)
print ('The largest prime factor is ', primefactors[0])



    
