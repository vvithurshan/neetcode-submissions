from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.Follow = defaultdict(set)
        self.Tweet = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.Tweet[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        if userId not in self.Follow:
            feeds = []
            # not following anyone
            for i in range(len(self.Tweet[userId]) - 1, -1, -1):
                feeds.append(self.Tweet[userId][i][1])

                if len(feeds) == 10:
                    break

            return feeds

        # if following
        minheap = []

        for tweet in self.Tweet[userId]:
            heapq.heappush(minheap, (tweet[0], tweet[1]))

            if len(minheap) > 10:
                heapq.heappop(minheap)

        for follow in self.Follow[userId]:
  
            for i in range(len(self.Tweet[follow])):
                heapq.heappush(minheap, (self.Tweet[follow][i][0], self.Tweet[follow][i][1]))

                if len(minheap) > 10:
                    heapq.heappop(minheap)
        
        feed = []
        
        while minheap:
            feed.append(heapq.heappop(minheap)[1])

        return feed[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.Follow[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId in self.Follow:
            self.Follow[followerId].remove(followeeId)

            if len(self.Follow[followerId]) == 0:
                del self.Follow[followerId]