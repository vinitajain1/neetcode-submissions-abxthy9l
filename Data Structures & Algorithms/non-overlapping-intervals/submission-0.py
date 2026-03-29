class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        n = len(intervals)
        intervals.sort(key=lambda x:x[1])
        def dfs(i):
            maxIntervals = 1
            for j in range(i+1,n):
                if intervals[i][1]<=intervals[j][0]:
                    maxIntervals = max(maxIntervals,1+dfs(j))
            return maxIntervals
        return n - dfs(0)