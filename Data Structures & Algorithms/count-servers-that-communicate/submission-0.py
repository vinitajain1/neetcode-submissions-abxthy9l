class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_counts = [0]*len(grid[0])
        col_counts = [0]*len(grid)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    row_counts[col]+=1
                    col_counts[row]+=1
        servers = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    if row_counts[col] > 1 or col_counts[row] > 1:
                        servers+=1
        return servers