class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_seen = {}
        need = len(t)
        current = 0
        left = 0
        mc = float("inf")
        seen = {}
        wc = 0
        output = ''

        for ch in t:
            t_seen[ch] = t_seen.get(ch, 0) + 1
        
        for idx, ch in enumerate(s):
            if ch in t_seen:
                seen[ch] = seen.get(ch, 0) + 1
                if t_seen[ch] >= seen[ch]:
                    current+=1

            while current == need:
                mc = min (mc, wc)
                output = s[left:idx+1]
                left_ch = s[left]
                left+=1
                wc-=1

                if left_ch in seen:
                    seen[left_ch]-=1
                    if seen[left_ch] < t_seen[left_ch]:
                        current-=1
        return output



