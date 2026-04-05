import heapq

class MedianFinder:
    def __init__(self):
        self.maxh = []
        self.minh = []

    def addNum(self, num: int) -> None:
        if not self.minh or num >= self.minh[0]:
            heapq.heappush(self.minh, num)
        else:
            heapq.heappush(self.maxh, -num)

        if len(self.minh) - len(self.maxh) > 1:
            heapq.heappush(self.maxh, -heapq.heappop(self.minh))
        elif len(self.maxh) - len(self.minh) > 1:
            heapq.heappush(self.minh, -heapq.heappop(self.maxh))


    def findMedian(self) -> float:
        if len(self.minh) == len(self.maxh):
            return (self.minh[0] - self.maxh[0]) / 2
        elif len(self.minh) > len(self.maxh):
            return self.minh[0]
        else:
            return -self.maxh[0]