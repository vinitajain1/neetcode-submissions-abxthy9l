class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        availableRoom = [i for i in range(n)] # 0,1,2,3,4 # Min heap
        used = [] # min Heap (end,room)
        count = [0] * n  # Count of meetings for each room
        for start,end in meetings:
            while used and used[0][0]<=start:
                _,room = heapq.heappop(used) # pop meeting which are done
                heapq.heappush(availableRoom,room)
            # check if no room are available delay the current meeting
            if not availableRoom:
                endTime,room = heapq.heappop(used)
                end = endTime+(end-start)
                heapq.heappush(availableRoom,room)
            # Use the room for meeting
            room = heapq.heappop(availableRoom)
            heapq.heappush(used,(end,room))
            count[room]+=1
        return count.index(max(count))
