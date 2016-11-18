'''
Problem: Say you have several coins whose face value are $1, $3 and $5.
         How to get $N using as few coins as you can?
         
Extra  : What about $2, $3, $5? or $3, $5, $10?
'''

COIN_FACE_VALUE_LIST = [1, 3, 5]
COIN_FACE_VALUE_LIST_EX = [2, 3, 5]

def leastCoins(n):
    valueList = COIN_FACE_VALUE_LIST_EX
    d = [0]*(n+1)
    for i in range(1, n+1):
        compareList = []
        for value in valueList:
            if value <= i:
                if not d[i-value] == -1:
                    compareList.append(d[i-value]+1)
        if compareList:
            d[i] = min(compareList)
        else:
            d[i] = -1
    return d[n]

if __name__ == '__main__':
    print leastCoins(11)
    print leastCoins(17)
    print leastCoins(18)