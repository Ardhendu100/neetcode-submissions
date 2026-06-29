class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i, 0)+1
        
        for i in seen:
            if seen[i] == 1:
                return i
        