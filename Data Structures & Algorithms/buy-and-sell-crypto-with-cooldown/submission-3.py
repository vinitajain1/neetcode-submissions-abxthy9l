class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(idx,canBuy):
            if (idx,canBuy) in dp:
                return dp[(idx,canBuy)]
            if idx>=len(prices):
                return 0
            cooldown = dfs(idx+1,canBuy)
            if canBuy:
                cooldown = max(cooldown,dfs(idx+1,not canBuy)-prices[idx])
            else:
                cooldown = max(cooldown,dfs(idx+2,not canBuy)+prices[idx])
            dp[(idx,canBuy)] = cooldown
            return cooldown
        return dfs(0,True)