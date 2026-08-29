class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        heap = []
        res = []

        for n in nums: count[n] += 1

        for n, cnt in count.items():
            heapq.heappush(heap, (cnt, n))
            if len(heap) > k:
                heapq.heappop(heap)

        return [t[1] for t in heap]
