# http://blog.csdn.net/yutianzuijin/article/details/11499917/
# Take this as a problem to find the kth smallest number in 2 lists.
'''
Pseudo code:

def findKth(nums1, nums2, k):
    Always suppose that nums1 is not longer than nums2.
    if nums1 is empty than return the kth smallest number in nums2.
    if k == 1 then return the smaller one of the first element in 2 lists.
    
    Compare the k/2-1 th member of the 2 lists,
    If equals then return that number.
    If not, remove all the element whose index <= k/2-1 in the smaller one, and
    take it as a new list and call the function again, this time should find the
    k - xa th smallest number.
'''
# Time complexity: O(log(M+N))
# Space complexity: O(log(M+N))
def findKth(nums1, nums2, k):
    if len(nums1) > len(nums2):
        return findKth(nums2, nums1, k)
    if not nums1:
        return nums2[k-1]
    if k == 1:
        return min(nums1[0], nums2[0])
    
    xa = min(len(nums1), k/2)
    xb = k - xa
    
    if nums1[xa-1] == nums2[xb-1]:
        return nums1[xa-1]
    elif nums1[xa-1] < nums2[xb-1]:
        nums1_new = nums1[xa:]
        return findKth(nums1_new, nums2, k-xa)
    else:
        nums2_new = nums2[xb:]
        return findKth(nums1, nums2_new, k-xb)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        cnt = len(nums1) + len(nums2)
        if cnt%2 == 1:
            return findKth(nums1, nums2, cnt/2+1)
        else:
            x1 = findKth(nums1, nums2, cnt/2)
            x2 = findKth(nums1, nums2, cnt/2+1)
            return (float(x1) + float(x2))/2