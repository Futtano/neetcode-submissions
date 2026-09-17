class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        followees = self.followees[userId]
        timeline = list(self.tweets[userId])

        for f in followees:
            timeline.extend(self.tweets[f])
        
        most_recent_ten = []

        for el in timeline:
            if len(most_recent_ten) < 10:
                heapq.heappush(most_recent_ten, el)
            elif el[0] > most_recent_ten[0][0]:
                heapq.heapreplace(most_recent_ten, el)
        return [m[1] for m in sorted(most_recent_ten, key=lambda x: -x[0])]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)