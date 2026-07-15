class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mc = float("inf")
        wc = 0
        left = 0
        result = ""
        need = set(t)
        missing = len(t)
        seen = {}

        for right in range(len(s)):
            char = s[right]
            wc+=1
            if char in need:
                seen[char] = seen.get(char,0)+1
                if seen[char] == 1:
                    missing-=1
                
            while missing == 0:
                if right - left + 1 < mc:
                    mc = right - left + 1
                    result=s[left:right+1]
                    
                left_char = s[left]
                wc-=1
                if left_char in need:
                    if left_char in seen:
                        seen[left_char] = seen.get(left_char) - 1
                        if seen[left_char] == 0:
                            missing+=1
                
                left+=1
        return "" if mc == float("inf") else result


                
                
                
            
            

        