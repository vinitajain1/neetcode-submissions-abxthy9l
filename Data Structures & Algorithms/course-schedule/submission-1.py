class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0]*numCourses
        adj = {i:[] for i in range(numCourses)}
        for src,dst in prerequisites:
            adj[src].append(dst)
            indegree[dst]+=1
        queue = deque()
        for crs in range(numCourses):
            if indegree[crs]==0:
                queue.append(crs)
        
        finish=0
        while queue:
            crs = queue.popleft()
            finish+=1
            for nei in adj[crs]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        return finish==numCourses

