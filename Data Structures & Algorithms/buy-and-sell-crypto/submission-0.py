class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(len(prices)):

            while l < r and prices[r] - prices[l] < 0:
                l += 1

            maxProfit = max(maxProfit, prices[r] - prices[l])

        return maxProfit