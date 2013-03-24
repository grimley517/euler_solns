def get_sum(n):
    string = str(n)
    total = 0
    for char in string:
        total = total + (int(char)**5)
    return total
answers = []
for i in range (4149, 1000000):
    if i == get_sum(i):
        answers.append(i)
print (answers)
total =0
for answer in answers:
    total = total + answer
print (total)
