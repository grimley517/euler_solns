def meetsCondition(number):
    result = True
    for i in range (11,20):
        if number % i != 0:
            result = False; break
    return result
number = 2520
while not meetsCondition (number):
    number = number+2
print (number)
    
