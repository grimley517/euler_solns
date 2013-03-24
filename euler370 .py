import math
limit = 1000
triangles = 0
p=3
while p<limit:
    c=int(p/2)
    b=c-1
    while c>b:
        a=c-b
        while b>a:
            a=c-b
            if (b**2)==(c*a):
                triangles = triangles +1
            b=b-1
        c=c-1
    
    p= p+1
    


print (triangles)
