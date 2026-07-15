class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_value = []
        

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        if len(self.stack) == 1:
            self.min_value.append(self.stack[-1])
        else:
            self.min_value.append(min(val, self.min_value[-1]))
        
        

    def pop(self) -> None:
        if self.stack[-1] == self.min_value[-1]:
            self.min_value.pop()

        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_value[-1]
        
