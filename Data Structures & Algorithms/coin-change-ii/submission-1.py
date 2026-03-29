class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        coins.sort()
        dp = {}
        def dfs(index,amount):
            if index>=len(coins) or amount<0:
                return 0
            if amount==0:
                return 1
            if (index,amount) in dp:
                return dp[(index,amount)]
            ways = 0
            ways = ways + dfs(index,amount-coins[index]) + dfs(index+1,amount)
            dp[(index,amount)] = ways
            return ways
        return dfs(0,amount)