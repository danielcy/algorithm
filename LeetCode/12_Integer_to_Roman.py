# Roman Number - Number:
'''
1   - I
5   - V
10  - X
50  - L
100 - C
500 - D
1000- M
'''

def singleDigit(num, c1, c2, c3):
    if num < 4:
        return num * c1
    elif num == 4:
        return c1 + c2
    elif num < 9:
        return c2 + (num-5) * c1
    else:
        return c1 + c3
        
def integer2roman(num):
    numstr = str(num)
    tnumstr = numstr[::-1]
    result = ''
    for i, c in enumerate(tnumstr):
        if i == 0:
            result = singleDigit(int(c), 'I', 'V', 'X') + result
        elif i == 1:
            result = singleDigit(int(c), 'X', 'L', 'C') + result
        elif i == 2:
            result = singleDigit(int(c), 'C', 'D', 'M') + result
        else:
            result = singleDigit(int(c), 'M', '', '') + result
    return result
    
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = integer2roman(num)
        return result
    
'''
Pretty Nice Solution:

M = ["", "M", "MM", "MMM"];
C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];

'''