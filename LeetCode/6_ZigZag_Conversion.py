# Well...This is not a hard issue...No comment on this.
# Time complexity: O(N)
# Space complexity: O(N)

def zigZagConvert(str, numRows):
    mode = 0
    l = len(str)
    if numRows == 1:
        return str
    zigZagList = []
    for rows in range(numRows):
        zigZagList.append('')
    
    markX = 0
    
    for i in range(l):
        zigZagList[markX] = zigZagList[markX] + str[i]
        if mode == 0:
            if markX == numRows - 1:
                mode = 1
                markX = markX - 1
            else:
                markX = markX + 1
        elif mode == 1:
            if markX == 0:
                mode = 0
                markX = markX + 1
            else:
                markX = markX - 1
    
    result = ''
    for line in zigZagList:
        result = result + line
    return result

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = zigZagConvert(s, numRows)
        return result