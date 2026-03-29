class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = {i:[] for i in range(numCourses)}
        for crs,preReq in prerequisites:
            preReqMap[crs].append(preReq)
        
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            visitSet.add(crs)
            for preReq in preReqMap[crs]:
                if not dfs(preReq):
                    return False
            visitSet.remove(crs)
            preReqMap[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        