class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            profit = max(profit,prices[i]-minBuy)
            minBuy = min(minBuy,prices[i])
        return profit