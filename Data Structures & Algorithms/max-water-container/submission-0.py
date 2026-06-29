class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        start = 0
        end =  len(heights) - 1
        while(start<=end):
            m =  min(heights[start], heights[end])
            area = max(area, m * (end - start))

            if m == heights[start]:
                start+=1
            else:
                end -=1
        return area