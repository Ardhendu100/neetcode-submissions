class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        if not (top <= bot):
            return False
        
        r, c = 0, cols - 1
        while r <= c:
            m = (r + c) // 2
            if target > matrix[mid][m]:
                r = m + 1
            elif target < matrix[mid][m]:
                c = m - 1
            else:
                return True
        return False

            

        