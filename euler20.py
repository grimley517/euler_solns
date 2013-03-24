def factorial(number):
    sum = 0
    while number !=0:
        sum=sum+number
        number = number +1
    print(number, ' factorial is ', sum)
    return sum

stringNum = str(factorial(100))
for char in stringNum:
    sum=0
    sum = sum + int(char)
print ('sum of characters = ', sum)
