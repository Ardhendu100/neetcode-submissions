class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_seen = {}
        t_seen = {}

        if len(s) != len(t):
            return False

        for i in s:
            s_seen[i] = s_seen.get(i,0)+1
        
        for i in t:
            t_seen[i] = t_seen.get(i,0)+1
        
        return s_seen == t_seen