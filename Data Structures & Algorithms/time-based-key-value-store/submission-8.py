class TimeMap:

    def __init__(self):
        self.maps = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.maps[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        updates = self.maps[key]

        if not updates: return ""
        if timestamp >= updates[-1][0]: return updates[-1][1]
        if timestamp < updates[0][0]: return ""

        l, r, hit = 0, len(updates) - 1, ""
        while l <= r:
            mid = (l + r) // 2
            time = updates[mid][0]

            if timestamp == time: return updates[mid][1]
            if timestamp > time:
                hit = updates[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return hit
        
