class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dfs(step):
            if step in dp:
                return dp[step]
            if step>n:
                return 0
            if step==n:
                return 1
            dp[step] = dfs(1+step)+dfs(2+step)
            return dp[step]
        
        return dfs(1) + dfs(2)