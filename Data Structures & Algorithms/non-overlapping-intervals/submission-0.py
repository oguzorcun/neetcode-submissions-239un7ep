class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2: return 0
        intervals.sort(key = lambda x: x[1])
        kept = [intervals[0]]

        for i in intervals[1:]:
            if i[0] >= kept[-1][1]: kept.append(i)
        
        return len(intervals) - len(kept)

