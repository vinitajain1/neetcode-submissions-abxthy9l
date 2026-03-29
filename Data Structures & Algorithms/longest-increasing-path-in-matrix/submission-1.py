class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        m,n = len(matrix),len(matrix[0])
        dp = {}
        def dfs(i,j,prev):
            if i<0 or j<0 or i>=m or j>=n or prev>=matrix[i][j]:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            dp[(i, j)] = 1 + max(
        dfs(i, j-1, matrix[i][j]),
        dfs(i, j+1, matrix[i][j]),
        dfs(i-1, j, matrix[i][j]),
        dfs(i+1, j, matrix[i][j])
    )
            return dp[(i,j)]

        for i in range(m):
            for j in range(n):
                dfs(i,j,-1)
        return max(dp.values())



