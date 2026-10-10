class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxedProfit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxedProfit = max(profit, maxedProfit)
            else:
                buy = sell
            sell += 1
        return maxedProfit