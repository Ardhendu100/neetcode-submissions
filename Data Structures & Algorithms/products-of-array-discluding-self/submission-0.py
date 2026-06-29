class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = []
        result = []
        c= 1
        for i,value in enumerate(nums):
            if not temp:
                temp.append([value,1])
            else:
                temp.append([value, (temp[i-1][0] * temp[i-1][1])])
                
        for i,value in temp[::-1]:
            if not result:
                result.append(value)
                
            else:
                result.append(value * c)
            c*=i
        return result[::-1]




        