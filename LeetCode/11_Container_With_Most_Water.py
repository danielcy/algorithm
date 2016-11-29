# This problem can be considered as a DP problem.
# A single DP solution:
'''
def getMaxArea(height):
    length = len(height)
    d = [[0, [0, 0]]] * length
    d[0] = [0, [0, 0]];
    d[1][0] = calculateArea(height, 0, 1)
    d[1][1] = [0, 1]
    
    for j in range(2, length):
        tempMax = 0
        index = 0
        for i in range(0, j):
            area = calculateArea(height, i, j)
            if area > tempMax:
                tempMax = area
                index = i
        d[j][0] = max(tempMax, d[j-1][0])
        d[j][1] = [index, j]
        
    return d[length-1]
    
def calculateArea(height, i, j):
    area = min(height[i], height[j]) * (j - i)
    return area
    
print getMaxArea(height)
'''
# The time complexity is O(N^2), Time Limit Exceeded.
# So we can use a method called 2 point approach:
# We take two pointers, one at the beginning and one at the end of the array 
# constituting the length of the lines. Futher, we maintain a variable 
# maxareamaxarea to store the maximum area obtained till now. At every step, we 
# find out the area formed between them, update maxareamaxarea and move the 
# pointer pointing to the shorter line towards the other end by one step.

def pointApproach(height):
    i = 0
    j = len(height)-1
    maxArea = 0
    while not i == j:
        currentArea = calculateArea(height, i, j)
        if currentArea > maxArea:
            maxArea = currentArea
        if height[i] >= height[j]:
            j = j - 1
        else:
            i = i + 1
    return maxArea
        
def calculateArea(height, i, j):
    area = min(height[i], height[j]) * (j - i)
    return area

print pointApproach(height)