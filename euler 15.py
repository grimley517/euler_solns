matrix = [[1]*21,]
line=1
while line<21:
    matrix.append([])
    for item in matrix[line-1]:
        matrix[line].append(item)
        matrix
    print(matrix[line])
    line = line +1
for i in range (1,21):
    for j in range(1,21):
        matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
for i in range (0,21):
    print (matrix[i])
