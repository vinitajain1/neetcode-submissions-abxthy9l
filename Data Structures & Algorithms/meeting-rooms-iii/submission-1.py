class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = []
        for i in range(n):
            heapq.heappush(rooms,i)
        res = [0]*n
        meetings.sort()
        used = []
        time = 0
        for start,end in meetings:
            while used and used[0][0]<=start:
                _,room = heapq.heappop(used)
                heapq.heappush(rooms,room)
            if not rooms:
                endTime,room = heapq.heappop(used)
                end = endTime+(end-start)
                heapq.heappush(rooms,room)
            avail = heapq.heappop(rooms)
            heapq.heappush(used,[end,avail])
            res[avail]+=1
        
        return res.index(max(res))