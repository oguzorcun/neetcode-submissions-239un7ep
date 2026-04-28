class Solution:
    def rob_rec(self, nums: List[int]) -> int:
        
        def rob(i: int):
            if i >= len(nums):
                return 0
            return max(rob(i + 1), nums[i] + rob(i + 2))
        
        return rob(0)

    def rob_memo(self, nums: List[int]) -> int:

        memo = [-1] * len(nums)

        def rob(i: int):
            if i >= len(nums): return 0
            if memo[i] != -1: return memo[i]
            memo[i] = max(rob(i + 1), nums[i] + rob(i + 2))
            return memo[i]

        return rob(0)

    def rob_dp(self, nums: List[int]) -> int:

        if len(nums) <= 2: return max(nums)

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return max(dp)

    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2: return max(nums)

        rob1, rob2 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            rob1, rob2 = rob2, max(rob1 + nums[i], rob2)

        return rob2









