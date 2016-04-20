import numpy as np

def sumrec(n):
    if n == 0: return n
    return pow(n, 3) + sumrec(n-1)

''' tests to make sure it works '''
def sumit(n):
    sum = 0;
    for i in range(1, n+1):
         sum += pow(i, 3)
    return sum
    
try:
    for i in range(1, 20):
        assert sumrec(i) == sumit(i)
        print 'test - sumrec({}): working'.format(i)
except AssertionError:
    print 'not working'
