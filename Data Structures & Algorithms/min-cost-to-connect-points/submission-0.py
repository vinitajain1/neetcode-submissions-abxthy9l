import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minHeap = [(0, tuple(points[0]))]
        mst = 0

        def getDist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        while minHeap:
            dist1, point1 = heapq.heappop(minHeap)

            if point1 in visited:
                continue

            visited.add(point1)
            mst += dist1

            for point2 in points:
                t_point2 = tuple(point2)

                if t_point2 in visited:
                    continue

                dist2 = getDist(point1, t_point2)
                heapq.heappush(minHeap, (dist2, t_point2))

        return mst