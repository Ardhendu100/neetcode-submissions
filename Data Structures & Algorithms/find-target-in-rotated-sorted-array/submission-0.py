class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(start, end):
            mid = start + ((end-start) // 2)
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            return -1

        
        start = 0
        end = len(nums)-1
        mid = start + ((end-start) // 2)
        if nums[mid] == target:
            return mid

        firstValue = bs(start, mid -1)
        if firstValue != -1:
            return firstValue
        else:
            lastValue = bs(mid+1, end)
            return lastValue

