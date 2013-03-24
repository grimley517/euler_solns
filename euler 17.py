def digitLength(number):
    length = 0
    if number ==1 or 2 or 6:
        length = 3
        elif number == 3 or 7 or 8:
            length = 5
        elif number == 4 or 5 or 9:
            length = 4
    return length
answer = 0
for num in range (1001):
    number = str(number)
    numberLength = 0
    if len(number)>2:
        if number[-2] ==1:
            numberLength = numberLength +4
            elif number[-2] ==0:
                numberLength = numberLength
            else:
                numberLength = numberLength +2
    if len(number)
    for each digit in number:
        
    
