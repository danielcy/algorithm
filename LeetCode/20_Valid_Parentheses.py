# Using stack to solve this problem.

def isValid(s):
    stack = []
    dic = {']': '[', '}': '{', ')': '('}
    for char in s:
        if char in dic.values():
            stack.append(char)
        elif char in dic.keys():
            if stack == [] or not dic[char] == stack.pop():
                return False
        else:
            return False
    return stack == []
    
# But I prefer this solution:

def isValid_v2(s):
    n = len(s)
    if n == 0:
        return True
    if n % 2 == 1:
        return False
        
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
        
    if s == '':
        return True
    else:
        return False