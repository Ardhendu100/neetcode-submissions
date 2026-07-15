class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(', '{', '['}
        stack = []
        flag = False
        for i in s:
            if i in brackets:
                stack.append(i)
            else:
                if i == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                        flag = True
                    else:
                        return False
                elif i == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                        flag = True
                    else:
                        return False

                if i == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                        flag = True
                    else:
                        return False
        return flag
        