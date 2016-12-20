# First try: For every num in nums, set list behind as lb. Using 3Sum method in problem 15 to make num + 3Sum == target.

def get3Sum(nums, target):
    result = []
    nums.sort()
    for i, num in enumerate(nums):
        if i > len(nums) - 3:
            break
        l = i+1
        r = len(nums)-1
        while not l == r:
            s = nums[i] + nums[l] + nums[r]
            if s < target:
                l = l + 1
            elif s > target:
                r = r - 1
            else:
                tempResult = [nums[i], nums[l], nums[r]]
                tempResult.sort()
                if not tempResult in result:
                    result.append(tempResult)
                l = l + 1
    return result
    
def get4Sum(nums, target):
    result = []
    for i, num in enumerate(nums):
        if i > len(nums) - 4:
            break
        listBehind = nums[i+1:]
        all3Sums = get3Sum(listBehind, target-num)
        for element in all3Sums:
            element.append(num)
            element.sort()
            if not element in result:
                result.append(element)
    return result
    
# Accepted.