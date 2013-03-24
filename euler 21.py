import math
def divisors (number):
    answers = []
    for i in range(1,int(math.sqrt(number)+1)):
        if number % i == 0:
            answers.append(i)
            answers.append(number/i)
    answers.remove(number)
    total = 0
    for answer in answers:
        total = total + answer
    return int(total)

amicables=[]
for n in range(1,10000):
    m= divisors (n)
    if n==divisors(m) and n!=m  :
        amicables.append(n)

total1 = 0
for amicable in amicables:
    total1 = total1 + amicable

print (amicables)
print (total1)
