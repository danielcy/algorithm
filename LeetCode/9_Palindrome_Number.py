# This problem is weird. What means no extra space? If it means O(1), then it's 
# too easy to solve, just get the reverse integer and compare. But if it means 
# no other variable, then it's impossible to do this in a efficient way.
# Well, anyway, they mark the difficulty as easy, so I'm not going to think too 
# much, lol.
# Time complexity: O(1)
# Space complexity: O(1)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        rs = s[::-1]
        rx = int(rs)
        if x == rx:
            return True
        else:
            return False