class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        intervals.sort()
        res = 0
        prevIntervalEnd = intervals[0][1]

        for start,end in intervals[1:]:
            if start>=prevIntervalEnd:
                prevIntervalEnd=end
            else:
                res+=1
                prevIntervalEnd = min(end,prevIntervalEnd)
        return res
