class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        end = max(piles)
        start = 1
        k = end

        while start <= end:
            mid = (start + end) // 2
            time = 0
            for p in piles:
                time += math.ceil(p/mid)
            if time <= h:
                k = mid
                end = mid - 1
            else:
                start = mid + 1
        return k




        