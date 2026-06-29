class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mc  = 0
        wc = 0
        l = 0
        count = {}
        for r in range(len(s)):
            wc+=1
            count[s[r]] = count.get(s[r], 0) + 1

            while wc - max(count.values()) > k:
                count[s[l]] -= 1
                l+=1
                wc-=1

            mc = max(mc, wc)
        return mc
        

        