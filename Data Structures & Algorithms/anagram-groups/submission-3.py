class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for ch in strs:
            tmp = "".join(sorted(ch))
            seen[tmp].append(ch)
        return list(seen.values())

        
