class Twitter:
    def __init__(self):
        self.tweetCounter = 0
        self.tweets = []
        self.users = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetCounter += 1
        heapq.heappush(self.tweets, (-self.tweetCounter, tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        tweets = self.tweets.copy()

        while tweets:
            t = heapq.heappop(tweets)
            if t[2] == userId or t[2] in self.users[userId]:
                feed.append(t[1])
                if len(feed) == 10: return feed
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        
