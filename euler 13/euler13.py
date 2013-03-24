numbers=[]
file=open('euler13input.txt')
eof=False
while not eof:
    string = file.readline()
    if string !='':
        numbers.append(int(string [0:12]))
    else:
        eof=True
sum = 0
for numner in numbers:
    sum = sum + numner
print (sum)
