class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        directions = [[1,0],[0,1]]
        dp = {}

        def dfs(i,j):
            if(i<0 or i>=m or j<0 or j>=n):
                return 0
            if i==m-1 and j==n-1:
                return 1
            key = str(i) + "_" + str(j)
            if key in dp:
                return dp[key]
            paths = 0
            for dr,dc in directions:
                paths = paths + dfs(i+dr,j+dc)
            dp[key] = paths
            return paths

        return dfs(0,0)




