class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in "+-*/":
                stack.append(int(ch))
            else:
                if ch == '+':
                    stack.append(stack[-1] + stack[-2])
                    print("--", stack)
                elif ch == '-':
                    stack.append(abs(stack[-1] - stack[-2]))
                elif ch == '*':
                    stack.append(stack[-1] * stack[-2])
                else:
                    a = (stack[-1] // stack[-2]) if stack[-1] > stack[-2] else stack[-2] // stack[-1]
                    print(a)
                    stack.append(a)
                
                stack.pop(-2)
                stack.pop(-2)
        return stack[0]