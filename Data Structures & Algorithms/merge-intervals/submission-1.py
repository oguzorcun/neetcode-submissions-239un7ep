class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]: # overlap
                merged[-1][1] = max(end, merged[-1][1])
            else:
                merged.append([start, end])
        
        return merged