# First try: Use the same logic as problem 15 to get the temp sum s. Compare each s and the target to find the closest one.

def get3Sum(nums, target):
    tempMin = 99999
    result = 0
    nums.sort()
    for i, num in enumerate(nums):
        if i > len(nums) - 3:
            break
        l = i+1
        r = len(nums)-1
        while not l == r:
            s = nums[i] + nums[l] + nums[r]
            d = abs(s - target)
            if d == 0:
                return s
            if d < tempMin:
                tempMin = d
                result = s
            if s < target:
                l = l + 1
            elif s > target:
                r = r - 1
    return result
    
# Accepted.