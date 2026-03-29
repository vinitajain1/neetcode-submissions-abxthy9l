"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key = lambda x:x.start)
        minHeap = []
        for i in range(len(intervals)):
            currStart = intervals[i].start
            currEnd = intervals[i].end
            if minHeap and minHeap[0]<=currStart:
               heapq.heappop(minHeap)
            heapq.heappush(minHeap,currEnd)
        return len(minHeap)