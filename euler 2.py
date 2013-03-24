fibbo = [1, 1]
while fibbo[len(fibbo)-1]<4000000:
    fibbo.append((fibbo[len(fibbo)-1]+fibbo[len(fibbo)-2]))
del fibbo[len(fibbo)-1]
sum = 0
for item in fibbo:
    if item %2 != 0:
        fibbo.remove(item)
    else:
        sum = sum + item
print (sum)
