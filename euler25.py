def correct (number):
    if len(str(number))==1000:
        return True
    else:
        return False
def FNo(fn, fn1):
    return fn +fn1
sequence =[0,1]
while not correct(sequence[len(sequence)-1]):
    index=len(sequence)-1
    sequence.append(FNo(sequence[index],sequence[index-1]))
for i in range(1,10):
    print( sequence[len(sequence)-i] )
print(len(sequence))
