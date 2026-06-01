class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        queue = deque([(sr,sc)])
        visit = set()
        m = len(image)
        n = len(image[0])
        res = [[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = image[i][j]
        while queue:
            r,c = queue.popleft()
            visit.add((r,c))
            for dr,dc in directions:
                row,col = r+dr,c+dc
                if row>=0 and row<m and col>=0 and col<n and image[row][col]==image[r][c] and not (row,col) in visit:
                    queue.append((row,col))
                    res[row][col] = color
            res[r][c] = color
        return res