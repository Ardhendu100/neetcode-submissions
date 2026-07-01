class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] 
        m = 0
        for idx, val in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > val:
                i, h = stack.pop()
                m = max(m, h * (idx-i))
                start = i
            
            stack.append((start, val))
        for i,h in stack:
            m = max(m, h * (len(heights) - i))
        return m
                


            

        
            
