meetreqs = []
pallnums=[]
a=3
b=2
def conditionmeet():
    answer=False
    for number in pallnums:
        if pallnums.count(number)==4:
            meetreqs.append(number)
    if len(meetreqs) == 5:
        answer = True
    return answer
conditionmet=conditionmeet()
while not conditionmet:
    for b in range (2,a):
        test = a**2 + b**3
        if str (test) == str(test)[::-1]:
            pallnums.append(test)
            print(test)
    a=a+1
    conditionmet = conditionmeet()
print(meetreqs)
total=0
for number in meetreqs:
    total = total+number
print(total)
    
