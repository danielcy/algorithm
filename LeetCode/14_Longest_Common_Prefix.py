def getLongestCommonPrefix(strs):
    result = ''
    try:
        i = 0
        while strs:
            temp = ''
            for str in strs:
                if not temp:
                    temp = str[i]
                elif not temp == str[i]:
                    raise IndexError
            result = result + temp
            i = i + 1
    except IndexError:
        pass
    return result

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = getLongestCommonPrefix(strs)
        return result
        