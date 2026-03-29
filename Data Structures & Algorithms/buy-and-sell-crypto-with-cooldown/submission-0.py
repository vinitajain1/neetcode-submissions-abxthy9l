class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        def dfs(index,canBuy):
            if index>=len(prices):
                return 0
            cooldown = dfs(index+1,canBuy)
            if canBuy:
                buy = dfs(index+1,False) - prices[index]
                return max(buy,cooldown)
            else:
                sell = dfs(index+2,True) + prices[index]
                return max(sell,cooldown)

        return dfs(0,True)