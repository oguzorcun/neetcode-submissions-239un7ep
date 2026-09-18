class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count, heap = defaultdict(int), []

        for n in nums: count[n] += 1

        for n, cnt in count.items(): heapq.heappush_max(heap, (cnt, n))

        return [heapq.heappop_max(heap)[1] for _ in range(k)]
