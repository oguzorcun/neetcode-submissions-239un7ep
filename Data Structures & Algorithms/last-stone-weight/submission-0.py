class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): stones[i] *= -1
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x == y: continue
            if x > y: heapq.heappush(stones, y - x)
            else: heapq.heappush(stones, x - y)
        
        return 0 if not stones else -stones[0]



