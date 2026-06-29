class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        result = []
        c = 0

        for i, str in enumerate(strs):
            sorted_str = ''.join(sorted(str))
            if seen.get(sorted_str) is None:
                seen[sorted_str] = c
                result.append([str])
                c+=1
            else:
                result[seen[sorted_str]].append(str)
        
        return result 
            


        