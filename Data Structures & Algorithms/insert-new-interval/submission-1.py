class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        finalArr = []
        for i, interval in enumerate(intervals):
            if interval[1]<newInterval[0]:
                finalArr.append(interval)
            elif interval[0]>newInterval[1]:
                finalArr.append(newInterval)
                return finalArr+intervals[i:]
            else:
                newInterval = [min(interval[0],newInterval[0]),max(interval[1],newInterval[1])]
        finalArr.append(newInterval)
        return finalArr