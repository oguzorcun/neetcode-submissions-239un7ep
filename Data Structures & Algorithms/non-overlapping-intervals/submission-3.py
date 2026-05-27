class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2: return 0
        intervals.sort(key = lambda x: x[1])
        end = intervals[0][1]
        skip = 0

        for i in intervals[1:]:
            if i[0] >= end: 
                end = i[1]
            else: 
                skip += 1
        
        return skip

