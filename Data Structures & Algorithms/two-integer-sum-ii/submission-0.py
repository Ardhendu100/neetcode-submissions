class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end =  len(numbers) - 1
        while (start<=end):
            if numbers[start] + numbers[end] == target and numbers[start] != numbers[end]:
                return [numbers[start], numbers[end]]
            elif numbers[start] + numbers[end] > target:
                end-=1
            else:
                start+=1
