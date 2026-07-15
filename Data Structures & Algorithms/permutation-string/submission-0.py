class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_seen = {}
        temp = 0
        left = 0
        s2_seen = {}
        for char in s1:
            s1_seen[char] = s1_seen.get(char, 0) + 1
        for char in s2:
            if char in s1_seen:
                s2_seen[char] = s2_seen.get(char, 0) + 1
                if s1_seen[char] < s2_seen[char]:
                    s2_seen = {}
                    temp = 0
                else:
                    temp+=1
                    if temp == len(s1):
                        return True
        return s1_seen == s2_seen
                
                    
                



            
        
        