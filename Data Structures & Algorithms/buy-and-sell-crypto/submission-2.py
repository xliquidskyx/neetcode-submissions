class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = 0, 1

        while sell <= len(prices) - 1:
            profit = prices[sell] - prices[buy]
            if profit > 0:      
                max_profit = max(profit, max_profit)
            else:
                buy = sell
            sell += 1
        return max_profit
        