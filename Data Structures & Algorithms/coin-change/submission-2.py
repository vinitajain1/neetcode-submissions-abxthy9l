class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount==0:
                return 0
            minCoins = 1e9
            for coin in coins:
                if amount-coin>=0:
                    minCoins = min(minCoins,1 + dfs(amount-coin))
            memo[amount] = minCoins
            return minCoins
        minCoins = dfs(amount)
        return -1 if minCoins>=1e9 else minCoins
        