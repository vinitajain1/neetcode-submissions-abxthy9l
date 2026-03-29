class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        pacific = set()
        atlantic = set()

        def dfs(r,c,prevHeight,visit):
            if(r<0 or c<0 or r>=rows or c>=cols or heights[r][c]<prevHeight or (r,c) in visit):
                return
            visit.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc,heights[r][c],visit)

        for c in range(cols):
            dfs(0,c,heights[0][c],pacific)

        for r in range(rows):
            dfs(r,0,heights[r][0],pacific)

        for c in range(cols):
            dfs(rows-1,c,heights[rows-1][c],atlantic)

        for r in range(rows):
            dfs(r,cols-1,heights[r][cols-1],atlantic)
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        
        return result
