class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        result = []
        for num in nums:
            seen[num] = seen.get(num, 0)+1
        sorted_items = sorted(seen.items(),key=lambda x:x[1],  reverse=True)
        for i in range(k):
            result.append(sorted_items[i][0])
        return result
        