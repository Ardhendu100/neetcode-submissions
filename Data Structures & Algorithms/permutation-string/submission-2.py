class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_seen = {}
        s1_l = len(s1)
        s2_seen = {}
        wc = 0
        left = 0
        for char in s1:
            s1_seen[char] = s1_seen.get(char, 0) + 1
        for char in s2:
            wc+=1
            s2_seen[char] = s2_seen.get(char, 0) + 1

            if wc == s1_l:
                if s1_seen == s2_seen:
                    return True
                else:
                    wc-=1
                    s2_seen[s2[left]] -= 1
                    if s2_seen[s2[left]] == 0:
                        del s2_seen[s2[left]]
                    left+=1
        return s1_seen == s2_seen



            
                
                    
                



            
        
        