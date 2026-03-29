class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [cnt for cnt in counter.values()]
        heapq.heapify_max(maxHeap)

        queue = deque()
        time = 0
        while maxHeap or queue:
            time+=1
            if not maxHeap:
                time = queue[0][1]
            else:
                topElem = heapq.heappop_max(maxHeap)
                elem = topElem - 1
                if elem>0:
                    queue.append([elem,time+n])
            if queue and queue[0][1] == time:
                heapq.heappush_max(maxHeap,queue[0][0])
                queue.popleft()
        
        return time
            