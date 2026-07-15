class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(', '{', '['}
        stack = []
        if len(s) == 1:
            return False
        for i in s:
            if i in brackets:
                stack.append(i)
            else:
                if i == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif i == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False

                if i == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        return True
        