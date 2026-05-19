class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i, jump in enumerate(nums):
            if i > max_reach: return False
            max_reach = max(max_reach, i + jump)

        return True

    def canJumpDP(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            dp[i] = any(dp[i + jump] for jump in range(1, nums[i] + 1) if i + jump < len(dp)) 

        print(dp)
        return dp[0]