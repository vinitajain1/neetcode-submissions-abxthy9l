class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        m,n = len(matrix),len(matrix[0])

        def dfs(i,j,prev):
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            if prev<matrix[i][j] or prev==-1:
                return max(dfs(i+0,j-1,matrix[i][j]),
                    dfs(i+0,j+1,matrix[i][j]),
                    dfs(i-1,j+0,matrix[i][j]),
                    dfs(i+1,j+0,matrix[i][j])) + 1
            return 0

        maxLen = 0
        for i in range(m):
            for j in range(n):
                maxLen = max(maxLen,dfs(i,j,-1))
        return maxLen



