class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}

        def dfs(index,canBuy):
            if index>=len(prices):
                return 0
            if (index,canBuy) in dp:
                return dp[(index,canBuy)]
            cooldown = dfs(index+1,canBuy)
            if canBuy:
                buy = dfs(index+1,False) - prices[index]
                dp[(index,canBuy)] = max(buy,cooldown)
            else:
                sell = dfs(index+2,True) + prices[index]
                dp[(index,canBuy)] = max(sell,cooldown)
            return dp[(index,canBuy)]

        return dfs(0,True)