# First try: Save the possible letter into a dictionary, and then get all possible result by visiting the dictionary.

mapping = dict()
mapping['2'] = 'abc'
mapping['3'] = 'def'
mapping['4'] = 'ghi'
mapping['5'] = 'jkl'
mapping['6'] = 'mno'
mapping['7'] = 'pqrs'
mapping['8'] = 'tuv'
mapping['9'] = 'wxyz'
mapping['0'] = ' '

def getAllCombinations(digits):
    result = []
    for i, digit in enumerate(digits):
        possibleLetters = mapping[digit]
        if result == []:
            for letter in possibleLetters:
                result.append(letter)
        else:
            newResult = []
            for element in result:
                for letter in possibleLetters:
                    newElement = element + letter
                    newResult.append(newElement)
            result = newResult
    return result
    
# Accepted.