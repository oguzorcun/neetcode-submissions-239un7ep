class Solution:
    def climbStairs(self, n: int) -> int:
        # prev, curr = 1, 1  # ways(1), ways(2)
        # for i in range(n - 1):
        #     prev, curr = curr, prev + curr
        # return curr

        if n <= 3: return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] 

        return dp[n]
