class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        maxarea = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if(r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0):
                return 0
            grid[r][c]=0
            return (1+dfs(r,c-1) +
                      dfs(r,c+1) +
                      dfs(r-1,c) +
                      dfs(r+1,c))
                    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    maxarea = max(dfs(r,c),maxarea)
        
        return maxarea