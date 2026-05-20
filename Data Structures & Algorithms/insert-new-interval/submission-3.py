class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        for i in range(len(intervals)):
            l, r, nl, nr = intervals[i][0], intervals[i][1], newInterval[0], newInterval[1]

            if nr < l:
                merged.append(newInterval)
                return merged + intervals[i:]
            if nl > r:
                merged.append(intervals[i])
            else:
                newInterval = [min(l, nl), max(r, nr)]
                
        merged.append(newInterval)
        return merged
