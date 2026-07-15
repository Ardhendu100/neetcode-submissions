class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        m = nums[0]
        while start <= end:
            if nums[start] < nums[end]:
                m = min(m, nums[end])
                return m
                
            mid = (start + end) // 2
            m = min(m, nums[mid])

            if nums[mid] >= nums[start]:
                start = mid + 1
                
            else:
                end = mid - 1
                
        return m
