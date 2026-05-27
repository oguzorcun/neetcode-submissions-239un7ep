class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2: return 0
        intervals.sort(key = lambda x: x[1])
        end = intervals[0][1]
        kept = 1

        for i in intervals[1:]:
            if i[0] >= end: 
                kept += 1
                end = i[1]
        
        return len(intervals) - kept

