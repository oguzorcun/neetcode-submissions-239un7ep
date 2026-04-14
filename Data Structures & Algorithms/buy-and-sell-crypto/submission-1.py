class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else: l = r
                
        return maxProfit