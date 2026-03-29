class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        q = deque()

        def addIsland(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==-1 or (r,c) in visit:
                return
            visit.add((r,c))
            q.append([r,c])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        dist = 0

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addIsland(r,c-1)
                addIsland(r,c+1)
                addIsland(r-1,c)
                addIsland(r+1,c)
            dist+=1


        