# First try: Get the sum of every 2 numbers in the list as X, find if -X is in the list, if so, add these 3 number to the result list.
'''
def get3Sum(nums):
    result = []
    for i, num in enumerate(nums):
        if i > len(nums) - 3:
            break
        listBehind = nums[i+1:]
        if num == 2:
            pass
        for j, element in enumerate(listBehind):
            temp2Sum = element + num
            if -temp2Sum in nums[:i]+nums[i+1:i+j+1]+nums[i+j+2:]:
                tempResult = [-temp2Sum, element, num]
                tempResult.sort()
                if not tempResult in result:
                    result.append(tempResult)
    return result
'''
# Time Limit Exceeded.
# A better solution: Sort nums first. For num in nums, set the list behind num as lb. Get the first element of lb as lb[l], and the last one as lb[r], calculate s = num + lb[l] + lb[r]. If s < 0 then move l, if s > 0 then move r, until s == 0.

def get3Sum(nums):
    result = []
    nums.sort()
    for i, num in enumerate(nums):
        if i > len(nums) - 3:
            break
        l = i+1
        r = len(nums)-1
        while not l == r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l = l + 1
            elif s > 0:
                r = r - 1
            else:
                tempResult = [nums[i], nums[l], nums[r]]
                tempResult.sort()
                if not tempResult in result:
                    result.append(tempResult)
                l = l + 1
    return result
        