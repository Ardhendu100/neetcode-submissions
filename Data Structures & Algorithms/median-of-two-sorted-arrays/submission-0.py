class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums = sorted(nums1)
        l = len(nums)
        
        if l%2 != 0:
            return nums[l // 2]
        else:
            m = (l-1) // 2
            n = m + 1
            return (nums[m] + nums[n]) / 2