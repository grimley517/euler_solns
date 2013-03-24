def ispal(number):
    result = False
    st = str(number)
    re = st[::-1]
    if st== re:
        result = True
    return result
largest = 0
for i in range (100,1000):
    for j in range (i,1000):
        prod = i*j
        if ispal(prod):
            if prod > largest:
                largest = prod

print (largest)
    
