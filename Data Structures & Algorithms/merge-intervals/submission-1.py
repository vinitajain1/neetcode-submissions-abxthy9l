class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        finalArr = []
        intervals.sort()
        for i,interval in enumerate(intervals):
            prevInterval = finalArr[-1] if finalArr else [0,0]
            if prevInterval[1]<interval[0]:
                finalArr.append(interval)
            else:
                if finalArr:
                    finalArr.pop()
                finalArr.append([min(prevInterval[0],interval[0]),max(prevInterval[1],interval[1])])
        return finalArr
                
