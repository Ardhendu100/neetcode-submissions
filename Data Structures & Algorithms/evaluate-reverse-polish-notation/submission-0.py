class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in "+-*/":
                stack.append(int(ch))
            else:
                if ch == '+':
                    stack.append(stack[0] + stack[1])
                elif ch == '-':
                    stack.append(abs(stack[0] - stack[1]))
                elif ch == '*':
                    stack.append(stack[0] * stack[1])
                else:
                    stack.append(stack[0] / stack[1])
                
                stack.pop(0)
                stack.pop(0)
        return stack[0]

        