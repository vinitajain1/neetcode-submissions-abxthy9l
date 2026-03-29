class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sub = 0
        dp = {}
        def dfs(i,j):
            nonlocal sub
            if (i,j) in dp:
                return dp[(i,j)]
            if j>=len(t):
                return 1
            elif i>=len(s):
                return 0
            sub = dfs(i+1,j)
            if s[i]==t[j]:
                sub+=dfs(i+1,j+1)
            dp[(i,j)] = sub
            return sub
            
        dfs(0,0)
        return sub
