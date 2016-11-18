'''
Problem: ZigZag      https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
         A sequence of numbers is called a zig-zag sequence if the differences
         between successive numbers strictly alternate between positive and negative.
         The first difference (if one exists) may be either positive or negative. 
         A sequence with fewer than two elements is trivially a zig-zag sequence.

         For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences 
         (6,-3,5,-7,3) are alternately positive and negative. In contrast, 1,4,7,2,5 
         and 1,7,4,5,5 are not zig-zag sequences, the first because its first two 
         differences are positive and the second because its last difference is zero. 
'''

def zigZag(numList):
    size = len(numList)
    difList = []
    for i in range(size):
        if size == 1:
            difList = numList[0]
            break
        if i > 0:
            difList.append(numList[i] - numList[i-1])
    d = [[1, 0]]*size
    for i in range(1, size):
        frontList = d[:i]
        temp = -1
        temp_s = 0
        for j in range(len(frontList)):
            dif = numList[i] - numList[j]
            if dif == 0:
                if temp < 1:
                    temp = 1
                    temp_s = 0
            elif dif * d[j][1] <= 0:
                if temp < d[j][0]+1:
                    temp = d[j][0]+1
                    if dif < 0:
                        temp_s = -1
                    else:
                        temp_s = 1
            else:
                if temp < 2:
                    temp = 2
                    if dif < 0:
                        temp_s = -1
                    else:
                        temp_s = 1
        d[i] = [temp, temp_s]
    resultList = [x[0] for x in d]
    result = max(resultList)
    return result
        
    
if __name__ == '__main__':
    testSample1 = [1, 7, 4, 9, 2, 5]
    testSample2 = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    testSample3 = [44]
    testSample4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    testSample5 = [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]
    testSample6 = [374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
                   600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
                   67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
                   477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
                   249, 22, 176, 279, 23, 22, 617, 462, 459, 244]
    print zigZag(testSample1)
    print zigZag(testSample2)
    print zigZag(testSample3)
    print zigZag(testSample4)
    print zigZag(testSample5)
    print zigZag(testSample6)