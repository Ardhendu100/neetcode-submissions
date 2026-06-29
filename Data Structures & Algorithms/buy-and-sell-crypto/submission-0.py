class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        max_profit = 0
        for i in prices:
            if i <= buy:
                buy = sell = i
                max_profit = max(max_profit, (sell-buy))
            else:
                sell = i
                max_profit = max(max_profit, (sell-buy))
        return max_profit
