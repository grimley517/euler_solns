sums = 0
sumsq = 0
for i in range (1, 101):
    sums = sums +i
    sumsq = sumsq + (i*i)
print ('the sum is', sums**2)
print ('the sum of squares is', sumsq)
print ('the difference is', sumsq - (sums*sums)) 
    
