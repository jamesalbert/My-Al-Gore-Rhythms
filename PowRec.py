def powrec(a, n):
    if n == 1: return pow(a, 2)
    return powrec(a, n-1) * powrec(a, n-1)


''' tests to make sure it works '''
try:
    for i in range(1, 20):
        assert powrec(i, i) == pow(i, pow(2, i))
        print 'test - powrec({}, {}): working'.format(i,i)
except AssertionError:
    print 'not working'
