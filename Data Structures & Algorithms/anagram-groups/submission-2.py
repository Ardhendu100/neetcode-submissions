class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for ch in strs:
            sorted_str = "".join(sorted(ch))
            if sorted_str in seen:
                seen[sorted_str].append(ch)
                
            else:
                seen[sorted_str]= [ch]
        return list(seen.values())