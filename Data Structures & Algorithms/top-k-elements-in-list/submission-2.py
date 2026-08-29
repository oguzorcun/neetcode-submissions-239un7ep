class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        max_heap = []
        res = []

        for n in nums: count[n] += 1

        for n, cnt in count.items():
            heapq.heappush(max_heap, (-cnt, n))
        
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])

        return res
