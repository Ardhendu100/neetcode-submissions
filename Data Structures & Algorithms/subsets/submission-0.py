class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # Choice 1: Take current number
            subset.append(nums[i])
            dfs(i+1)

            # undo the choice
            subset.pop()

            # skip the current number
            dfs(i+1)
        dfs(0)
        return res