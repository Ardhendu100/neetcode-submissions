class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = []
        for i in temperatures[::-1]:
            c =  1
            if len(stack) == 0:
                stack.append((i, 0))
                result.append(0)
            elif i < stack[-1][0]:
                stack.append((i, 1))
                result.append(1)
            else:
                while stack and stack[-1][0] <= i:
                    if stack[-1][1] == 0:
                        c=0
                    else:
                        c+=stack[-1][1]
                    stack.pop()
                stack.append((i,c))
                result.append(c)
        return result[::-1]



        