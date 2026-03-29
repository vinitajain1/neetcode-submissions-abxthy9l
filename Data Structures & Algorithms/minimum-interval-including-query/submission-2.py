class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        res = {}
        minHeap = []
        i = 0
        intervals.sort()
        for q in sorted(queries):
            for i in range(len(intervals)):
                if intervals[i][0] <= q:
                    l = intervals[i][0]
                    r = intervals[i][1]
                    heapq.heappush(minHeap,[r-l+1,r])
            while minHeap and q>minHeap[0][1]:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]