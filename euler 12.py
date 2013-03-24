import math
def tringle(number):
    result=int((number/2)*(number+1))
    return result
def factors(number):
    result=0
    for i in range (1,int(math.sqrt(number)+1)):
        if number%i==0:
            result = result +1
    return result*2
facts=0
tnum=1
while facts<500:
    tnum=tnum+1
    trinum = tringle(tnum)
    facts = factors(trinum)
    
    
print ('{0} is the {1}th triangle number and has {2} factors'.format(trinum,tnum,facts))
