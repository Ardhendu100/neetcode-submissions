class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            if count.get(n,0) == 1:
                return True
            count[n] = count.get(n,0) + 1   # “If key n exists, give me its value. Otherwise, give me 0. ”
                                            # Now that you got the previous count (or 0), you want to increase it by 1 because you’ve just seen that number once more.
        return False