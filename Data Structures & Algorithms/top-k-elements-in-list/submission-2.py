class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        result = []
        for i in nums:
            seen[i] = seen.get(i,0)+1
        
        for val in seen:
            if seen[val] >= k:
                result.append(val)
        return result


        