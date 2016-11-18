# Very easy to implement in python. One thing is, should notice it is an integer,
# so if the result > 0xffffffff/2 should set the result to 0.
# Time complexity: O(1)
# Space complexity: O(1)

def reverseInteger(i):
    if i >= 0:
        s = str(i)
    else:
        ri = -i
        s = str(ri) + '-'
    rs = s[::-1]
    result = int(rs)
    if abs(result) > 0xffffffff/2:
        return 0
    return result

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = reverseInteger(x)
        return result