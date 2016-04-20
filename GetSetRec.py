def getsetrec(n):
    s = []
    if n == 0: return s
    if n == 1:
        s.append('0')
        s.append('1')
        return s
    for x in getsetrec(n-1):
        y = '0{}'.format(x)
        s.append(y)
        y = '1{}'.format(x)
        s.append(y)
    return s

''' tests to make sure it works '''
try:
    for i in range(1, 20):
        assert len(getsetrec(i)) == pow(2, i)
        print 'test - {0,1}^%d: working' % i
except AssertionError:
    print 'not working'
