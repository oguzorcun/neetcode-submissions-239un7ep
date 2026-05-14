class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            cands = [dp[j] + 1 for j in range(i) if nums[i] > nums[j]]
            if cands: dp[i] = max(cands)

        return max(dp)