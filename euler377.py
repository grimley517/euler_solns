import <itertools>
def maxNum(i):
    answer = '1'
    for j in range (i-1):
        answer= answer +"1"
    return int(answer)
def expandList(lst):
    for element in lst:
        for i in range (len(str(element))-1):
            string = str(element)
            trial = int(string[i]) +int(string[i+1])
            if int(trial) <10:
                string.replace(string[i:(i+1)],str( trial),1)
                lst.append(string)
    return answer
def expandList2(lst):
    for element in lst:
        listAdd = itertools.permutations(str(element))
        for elem in listAdd:
            lst.append(int(elem))        
    return lst
def canExpand(lst):
    answer = False
    lst.sort(reverse=True)
    test = str(lst[0])
    if len(test)==1:
        return False
    for i in range(1,len(test)):
        if (int(test[i])+int(test[i-1]))<10:
            answer = True
    return answer
def fn(n):
    Startpoint =maxNum(n)
    lst=[Startpoint]
    while canExpand(lst):
        expandList(lst)
    expandList2(lst)
    for element in lst:
        while lst.count(element)>1:
            lst.remove(element)
    answer = 0
    for element in lst:
        answer = answer +element
    return answer
answer = 0
for i in range (1, 18):
    answer = answer +fn(i)
    print(i, ', ->  ', answer)
