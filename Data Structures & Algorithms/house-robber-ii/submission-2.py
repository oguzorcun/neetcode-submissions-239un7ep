# class Solution:
#     def rob(self, nums: List[int]) -> int:

#         if len(nums) <= 3: return max(nums)

#         return max(self.robCut(nums[1:]), self.robCut(nums[:-1]))

#     def robCut(self, nums: List[int]) -> int:

#         if len(nums) <= 2: return max(nums)
        
#         dp = [0] * len(nums)
#         dp[0], dp[1] = nums[0], max(nums[0], nums[1])

#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

#         return max(dp)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            memo[i][flag] = max(dfs(i + 1, flag),
                            nums[i] + dfs(i + 2, flag))
            return memo[i][flag]

        return max(dfs(0, True), dfs(1, False))