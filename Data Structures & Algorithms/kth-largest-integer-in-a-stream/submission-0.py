class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.h = nums.copy()
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        kth_min = len(self.h) - self.k + 1
        popped = [heapq.heappop(self.h) for _ in range(kth_min)]
        kth_min_num = popped[-1]
        for p in popped: heapq.heappush(self.h, p)
        return kth_min_num

