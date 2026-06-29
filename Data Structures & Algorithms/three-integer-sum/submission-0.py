class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for idx, val in enumerate(nums):
            if idx > 0 and nums[idx-1] == val:
                continue

            left, right = idx + 1, len(nums) - 1
            
            while left < right:
                total = nums[left] + nums[right] + val
                
                if total == 0:
                    res.append([nums[left],nums[right], val])
                    left+=1
                    while nums[left] == nums[left - 1] and left < right:
                        left+=1
                elif total > 0:
                    right -= 1
                else:
                    left+=1
        return res
            

