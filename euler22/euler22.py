import csv
file = csv.reader(open('names.txt'), delimiter =',')
names =[]
for row in file:
    for name in row:
        names.append(name)
names.sort()
chartots= []
for name in names:
    chartot=0
    for char in name:
        chartot = chartot + ord(char)-64
    chartots.append(chartot)
total = 0
position = 1
for tot in chartots:
    total = total + (tot * position)
    position = position +1
print (total)
