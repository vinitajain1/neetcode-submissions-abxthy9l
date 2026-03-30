class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(idx,amt):
            if (idx,amt) in dp:
                return dp[(idx,amt)]
            if idx>=len(coins) or amt<0:
                return 0
            if amt==0:
                return 1
            dp[(idx,amt)]=dfs(idx,amt-coins[idx])+dfs(idx+1,amt)
            return dp[(idx,amt)]
        return dfs(0,amount)