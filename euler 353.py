import math
def risk(d,r):
    output = pow((d/(r*math.pi)),2)
    return output
def paths (r):
    pathlist=[]
    for x in range(-r,r):
        for y in range(-r,r):
            for z in range(-r,r):
                if (x**2 +y**2 + z**2)==(r**2):
                    pathlist.append([x,y,z])
    paths = len(pathlist)
    print('r= {0}, path list'.format(r))
    print (pathlist)
    return paths
def Cfn(r):
    PathDistance =math.pi*r/paths (r)
    Mfn = paths(r) * risk(PathDistance,r)
    return Mfn
total = 0
for n in range (1,16):
    r = 2**n-1
    total = total + Cfn(r)
    print ('n= {0}, M = {1}, Total = {2}'.format(r, Cfn(r),total))
