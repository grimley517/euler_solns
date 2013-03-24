from math import sqrt, acos, pi

def solve(r):
    # find all stations
    r2 = r * r
    for i in range(0, int(sqrt(r2 / 3.0)) + 1):
        i2 = i * i
        for j in range(i, int(sqrt((r2 - i2) / 2.0)) + 1):
            k2 = r2 - i2 - j * j
            k = int(sqrt(k2))
            if k * k == k2:
                return [i, j, k]
                        
def risk(r, journey):
    r = float(r)
    a = 0
    risk = 0
    for z in journey:
        a1 = acos(z / r) / pi
        da = a1 - a
        risk += da * da
        a = a1
    if a < 0.5:
        return risk + (1 - a * 2) * (1 - a * 2)
    else:
        return risk * 2
        

if __name__ == '__main__':
    n = 3
    r = (1 << n) - 1
    print (n, r)
    c = 0
    for i, j, k in solve(r):
        print (i, j, k)
        print (risk(r, (i,)))
        print (risk(r, (j,)))
        print (risk(r, (k,)))
        c += 1
    print ('total: %d' % c)
