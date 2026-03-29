class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time,tweetId])
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        self.followers[userId].add(userId)
        for followeeId in self.followers[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId])-1
                count,tweetId = self.tweets[followeeId][index]
                heapq.heappush_max(maxHeap,[count,tweetId,followeeId,index-1])

        while maxHeap and len(res)<10:
            count,tweetId,followeeId,index = heapq.heappop_max(maxHeap)
            res.append(tweetId)
            if index>=0:
                count,tweetId = self.tweets[followeeId][index]
                heapq.heappush_max(maxHeap,[count,tweetId,followeeId,index-1])
        return res       

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
