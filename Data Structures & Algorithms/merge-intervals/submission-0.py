class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
                continue
            lastInterval = res[-1]
            currInterval = intervals[i]
            if lastInterval[1]<currInterval[0]:
                res.append(currInterval)
            else:
                res.pop()
                mergedInterval=[
                    min(lastInterval[0],currInterval[0]),
                    max(lastInterval[1],currInterval[1])
                ]
                res.append(mergedInterval)
        return res