import math
def divisors(number):
    divisors = []
    top = int(math.sqrt(number))+1
    for i in range (1,top):
        if number%i ==0:
            divisors.append (i)
            if i != 1:
                divisors.append (int(number / i))
    return divisors
def sumOfDivisors(number):
    total = 0
    for divisor in divisors(number):
        total = total + divisor
    return total
def abundants(number):
    abundants = []
    for i in range (12, number):
        if i < sumOfDivisors(i):
            abundants.append(i)
    return abundants
print ('check this for 28 ', divisors(28), ' add up to ', sumOfDivisors(28))
tarRange = []
for i in range (28123):
    tarRange.append(i)
    
abundantNos = abundants(28123)
print (len(abundantNos))
for i in abundantNos:
    for j in abundantNos:
        if (i+j) in tarRange:
            tarRange.remove(i+j)
    abundantNos.remove(i)
    print (len(abundantNos))
    
total = 0
for i in tarRange:
    total = total +i
print (tarRange)
print (total)
