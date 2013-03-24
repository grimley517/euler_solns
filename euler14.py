def function(n):
    if n % 2==0:
        result = n/2
    else:
        result = 3*n+1
    return result

maxcount = 20
for number in range(1000000,2,-1):
    stnumber=number
    count = 0
    while number !=1:
        number = function(number)
        count = count +1
    if count>maxcount:
        maxcount = count
        print( stnumber,' has a path of', count,' to 1')
        
