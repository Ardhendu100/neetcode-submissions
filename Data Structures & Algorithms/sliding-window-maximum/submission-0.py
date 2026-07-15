class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        wc = 0
        result = []
        seen = {}
        left = 0
        for num in nums:
            seen[num] = seen.get(num, 0)+1
            wc+=1
            if wc == k:
                mc = max(seen)
                result.append(mc)

                if mc == nums[left]:
                    seen[nums[left]]-=1
                    if seen[nums[left]] == 0:
                        del seen[nums[left]]
                left+=1
                wc-=1
        return result
                

        