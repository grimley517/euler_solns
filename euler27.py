import math
from collections import namedtuple
def eqn (a, b, n):
    return (n**2 +a*n +b)

def isprime (x):
    answer = True
    if x<2:
        answer = False
    if x>= 2:
        for i in range (2,x):
            if x % i == 0:
                answer = False
    return answer
primelist = []
for i in range (2,1001):
    if isprime(i):
        primelist.append(i)

answer = namedtuple('Answer',['a','b','primeLength'])
answers = []
for a in range (-1000,1001):
    for b in primelist:
        n=0
        while isprime(eqn(a,b,n)):
            n=n+1
        answers.append(answer(a, b, n))
ans = answer(0,0,0)
for a in answers:
    if a.primeLength>ans.primeLength:
        ans = a
print (ans)
print (ans.a * ans.b)
