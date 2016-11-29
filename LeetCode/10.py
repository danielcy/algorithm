'''
def isMatch(s, p):
    split p with "*", to get the list l that do not contain "*" and their preceding 
    element. Store the preceding elements into a list precList.
    
'''

def isMatch(s, p):
    prel = p.split('*')
    l = []
    precList = []
    for index, element in enumerate(prel):
        l.append(element[:-1])
        if not element == '':
            precList.append(element[-1])
        else:
            precList.append(element)
            
    precList = precList[:-1]
    
    subp = s
    checkIndex = 0
    for index, element in enumerate(l):
        if element == '':
            dupCount = 0
            for char in subp:
                if char == precList[checkIndex]:
                    dupCount = dupCount + 1
                else:
                    break
            if dupCount == 0:
                return False
            else:
                checkIndex = checkIndex + 1
                subp = subp[dupCount:]
                print dupCount
                print subp
                continue
        findex = subp.find(element)
        checksub = subp[:findex]
        if checksub:
            for char in checksub:
                if not char == precList[checkIndex]:
                    return False
            checkIndex = checkIndex + 1
        newStartIndex = len(element) + findex
        subp = subp[newStartIndex:]
        print newStartIndex
        print subp
        
    if subp == '':
        return True
    else:
        return False

s = 'abccdeeeffghiiij'
a = 'abc*de*f*ghi*j'
print isMatch(s, a)
        
        