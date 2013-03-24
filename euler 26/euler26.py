primelist = []
def isprime(x):
    if x<=1:
        return False
    else:
        for i in range (2,x):
            if x%i==0:
                return False
    return True
for i in range (1000):
    if isprime (i):
        primelist.append(i)
print (primelist)

def div_by(rem,div):
    y=min([x for x in range(5) if rem*(10**x)>div])
    return (rem*(10**y)%div)

for p in primelist:
    reciprocl = (1/float(p))
    
    print (str(p) + ' has a period ' + str(period)) 
