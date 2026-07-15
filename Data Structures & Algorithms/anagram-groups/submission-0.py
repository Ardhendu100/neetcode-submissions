class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        result = []

        for i, str in enumerate(strs):
            sorted_str = ''.join(sorted(str))
            if seen.get(sorted_str) is None:
                seen[sorted_str] = i
                result.append([str])
            else:
                result[seen[sorted_str]].append(str)
        
        return result 
            


        