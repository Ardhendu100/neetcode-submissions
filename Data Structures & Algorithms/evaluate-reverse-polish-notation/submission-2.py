class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in "+-*/":
                stack.append(int(ch))
            else:
                a = stack.pop()
                b = stack.pop()
                if ch == '+':
                    stack.append(a+b)
                elif ch == '-':
                    stack.append(abs(a-b))
                elif ch == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
        return stack[0]