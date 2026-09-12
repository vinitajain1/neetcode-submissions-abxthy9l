class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        interToRemove = 0
        intervals.sort()
        prevEnd = intervals[0][1]
        for start,end in intervals[1:]:
            if start>=prevEnd:
                prevEnd=end
            else:
                interToRemove+=1
                prevEnd=min(prevEnd,end)
        return interToRemove