class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = []
        for i in temperatures[::-1]:
            if not stack:
                stack.append((i, 0))
                result.append(0)
            else:
                c =  1
                while stack and stack[-1][0] <= i:
                    c+=stack[-1][1]
                    stack.pop()
                result.append(0 if not stack else c)
                stack.append((i,c))
                
        return result[::-1]



        