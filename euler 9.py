import math

a=1
b=2
#assume b>a
def getC(a,b):
    c = math.sqrt((a**2 +b**2))
    return c
c=getC(a,b)

while a+b+c != 1000:
    if a+b+c<1000:
        b=b+1
        c=getC(a,b)
    else:
        a=a+1
        b=a+1
        c=getC(a,b)
        
print ('a={0:1}, b={1:1}, c={2:1}'.format(a,b,c))
print(a*b*c)
    
