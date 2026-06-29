class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        mc = 0
        for idx,val in enumerate(s):
            if val in seen and seen[val] >= left:
                left = seen[val] + 1
            
            seen[val] = idx
            mc = max(mc, (idx-left+1))
        return mc
