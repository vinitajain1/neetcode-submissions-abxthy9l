class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price = prices[0]
        for p in prices[1:]:
            profit=max(profit,p-price)
            price = min(price,p)
        return profit
