class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s+='+'+i
        return s[1:]


    def decode(self, s: str) -> List[str]:
        return s.split('+')

