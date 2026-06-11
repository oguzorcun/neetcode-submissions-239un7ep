class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # def dfs(i: int):
        #     if i >= len(cost): return 0
        #     return cost[i] + min(dfs(i + 1), dfs(i + 2))
        
        # return min(dfs(0), dfs(1))

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])