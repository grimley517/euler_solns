TarNum = 200000
con = []
for i in range (2,TarNum):
    con.append(i)
def sumarray (array):
    sum = 0
    for fact in array:
        sum = sum +fact
    return sum
def findcops (number2):
    for number in con:
        if number<number2 and iscoprime (number, number2):
            con.remove(number)
        
def iscoprime(number, number2):
    answer = False
    for i in range (2,number+1):
        if number%i ==0 and number2%i==0:
            answer = True
    return answer
con.sort(reverse=True)
for number in con:
    findcops(number)
for number in con:
    findcops(number)
for number in con:
    findcops(number)
con.append(1)
print(con)
print(sumarray(con))
