class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        result = []
        for num in nums:
            seen[num] = seen.get(num, 0)+1
        for num in seen:
            if seen[num] >= k:
                result.append(num)
        return result
        