'''
Problem: em...Just the normal LIS problem, Google or Baidu for detail.
Extra  : The algorithm whose time complexity with O(Nlog(N))?(Not DP)
'''

def lis(numList):
    size = len(numList)
    d = [1]*size
    for i in range(1, size):
        num = numList[i]
        temp = -1
        frontList = d[:i]
        for j in range(len(frontList)):
            if frontList[j] >= temp and num > numList[j]:
                temp = frontList[j]
                d[i] = frontList[j] + 1
                
    return max(d)
    
if __name__ == '__main__':
    testSample1 = [5, 3, 4, 8, 6, 7]
    testSample2 = [6, 4, 5, 7, 8, 3, 9, 17, 19, 12, 13, 14, 15, 20]
    testSample3 = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    print lis(testSample1)
    print lis(testSample2) 
    print lis(testSample3)