# get 3s below 1000
threes = int(1000/3)
threes = (threes+1)*(threes/2)*3
# get 5s below 1000
fives = int(1000/5)-1
fives = (fives+1)*(fives/2)*5
# get 15s below 1000
fifteens = int(1000/15)
fifteens = (fifteens+1)*(fifteens/2)*15
#add the threes and fives, and subtract the fifteens
sum = threes + fives - fifteens
print (sum)
