class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for xi,yi in points:
            xj,yj = 0,0
            dist = ((xi-xj)**2 + (yi-yj)**2) ** 0.5
            heapq.heappush(minHeap,[dist,xi,yi])
        res = []
        while k!=0 and minHeap:
            dist,i,j = heapq.heappop(minHeap)
            res.append([i,j])
            k-=1
        return res
