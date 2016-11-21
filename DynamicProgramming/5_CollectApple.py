'''
Problem: There's a N*M map, with some apples on each lattice. Now from top left 
         corner, you can go right or down each time and collect the apple on the
         lattice. So give the max number of the apples you can collect on location
         (n, m)
'''
APPLE_MAP = [[1, 3, 5, 9, 13, 4, 2, 8],
             [7, 14, 5, 3, 1, 2, 4, 3],
             [28, 4, 0, 2, 3, 4, 23, 0],
             [1, 2, 9, 11, 17, 8, 0, 5]]
N = 4
M = 8
             
def getMaxApples(n, m):
    appleMap = APPLE_MAP
    maxn = N
    maxm = M
    d = []
    for x in range(maxn):
        d.append([0]*maxm)
    d[0][0] = appleMap[0][0]
    if n >= maxn or m >= maxm:
        print "Input Error."
        return -1
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                d[i][j] = d[i][j-1] + appleMap[i][j]
            elif j == 0:
                d[i][j] = d[i-1][j] + appleMap[i][j]
            else:
                d[i][j] = max(d[i-1][j], d[i][j-1]) + appleMap[i][j]
    import pprint
    pprint.pprint(d)
    return d[n][m]
    
    
if __name__ == '__main__':
    print getMaxApples(2,5)
        
        