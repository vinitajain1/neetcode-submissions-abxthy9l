class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh_count = 0

        def addFruit(r,c):
            nonlocal fresh_count
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0 or grid[r][c]==2:
                return
            q.append((r,c))
            grid[r][c] = 2
            fresh_count -= 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh_count += 1
        minutes = 0
        
        while q and fresh_count > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                addFruit(r,c-1)
                addFruit(r,c+1)
                addFruit(r-1,c)
                addFruit(r+1,c)
            minutes+=1
        return minutes if fresh_count == 0 else -1