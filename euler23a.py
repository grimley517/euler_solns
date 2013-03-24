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
    abundants = [0]
    for i in range (12, number):
        if i < sumOfDivisors(i):
            abundants.append(i)
    return abundants
print ('check this for 28 ', divisors(28), ' add up to ', sumOfDivisors(28))
    
abundantNos = abundants(28123)
canFit=[]
for i in abundantNos:
    for j in abundantNos:
        if int(i+j) not in canFit:
            canFit.append(i+j)
    
total = 0
for i in canFit:
    total = total +i
sumOfAll = (28123+1)*(28123/2)
print (sumOfAll - Total)
