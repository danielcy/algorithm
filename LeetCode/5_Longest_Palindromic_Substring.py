# http://www.cnblogs.com/bitzhuwei/p/Longest-Palindromic-Substring-Part-II.html
# Use Manacher Algorithm. 
'''
Pseudo code:

def manacher(str):
    newStr = insert '#' between every 2 characters in str
    define list p to save the radius of every characters
    define a center c index to prevent redundance calculate.
    for every characters char in newStr:
        if char is the first character then set p[0] to 0 amc go to the next
        character.
        if char is not the center, and if the reverse index of char exist and 
        p[ri] does not out of c's range,
        then let p[i] = p[ri] and go to the next character.
        
        Find the radius of palindromic substring which take char as the center.
        And set it to p[i].
        If the substring is out of c's range, set c = i.
        
    Find the longest palindromic substring according to list p.

'''
# Time complexity: O(N)
# Space complexity: O(N)
def manacher(str):
    newStr = preProcess(str)
    p = [0]*len(newStr)
    c = 1
    left = 0
    right = 2
    
    for i in range(len(newStr)):
        if i == 0:
            p[i] = 0
            continue
        if not c == i:
            ri = 2 * c - i
            if ri >= 0:
                if p[ri] < right - i:
                    p[i] = p[ri]
                    continue
        
        radius = 0
        try:
            while newStr[i-radius] == newStr[i+radius]:
                radius = radius + 1
            p[i] = radius - 1
        except IndexError:
            p[i] = radius - 1
            
        if p[i] >= right-i:
            c = i
            left = c - p[i]
            right = c + p[i]
    maxIndex = p.index(max(p))
    maxRadius = p[maxIndex]
    sub = newStr[maxIndex-maxRadius: maxIndex+maxRadius+1]
    result = sub.replace('#', '')
    return result
    
    
def preProcess(s):
    result = '#'
    for i in range(len(s)):
        result = result + s[i] + '#'
    return result

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = manacher(s)
        return result
        
        