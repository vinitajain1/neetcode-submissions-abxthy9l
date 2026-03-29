class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReqMap = {i:[] for i in range(numCourses)}
        for crs,preReq in prerequisites:
            preReqMap[crs].append(preReq)
        
        cycleSet = set()
        visitSet = set()

        courseSeq = []

        def dfs(crs):
            if crs in cycleSet:
                return False
            if crs in visitSet:
                return True
            cycleSet.add(crs)
            for preReq in preReqMap[crs]:
                if not dfs(preReq):
                    return False
            cycleSet.remove(crs)
            visitSet.add(crs)
            courseSeq.append(crs)
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return courseSeq