class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
            else:
                profit = -1
                l = r
            maxProfit = max(maxProfit, profit)
        return maxProfit