class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxedProfit = 0
        while sell <= len(prices) - 1:
            if prices[sell] - prices[buy] > 0:
                profit = prices[sell] - prices[buy]
                maxedProfit = max(maxedProfit, profit)
            else:
                buy = sell
            sell += 1
        return maxedProfit
            
            