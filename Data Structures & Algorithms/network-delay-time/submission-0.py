class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append([v,w])
        minHeap = [(0,k)]
        visit = set()
        time = 0

        while minHeap:
            weight,edge = heapq.heappop(minHeap)
            if edge in visit:
                continue
            visit.add(edge)
            time = max(time,weight)
            for v,w in edges[edge]:
                if v not in visit:
                    heapq.heappush(minHeap,(weight+w,v))
            
        return time if len(visit)==n else -1
        