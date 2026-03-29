class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = {i:[] for i in range(n)}
        for e1,e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)

        visited = set()

        def dfs(i):
            visited.add(i)
            for edge in adjList[i]:
                if edge not in visited:
                    dfs(edge)

        connected = 0
        for i in adjList:
            if i not in visited:
                connected+=1
                dfs(i)
        return connected