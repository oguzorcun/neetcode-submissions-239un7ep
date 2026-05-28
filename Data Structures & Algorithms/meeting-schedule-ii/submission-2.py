"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key = lambda interval: interval.start)
        h = [intervals[0].end]

        for ival in intervals[1:]:
            if ival.start >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h, ival.end)

        return len(h)
            
