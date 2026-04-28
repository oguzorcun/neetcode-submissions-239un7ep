class Solution:
    def rob_rec(self, nums: List[int]) -> int:
        
        def rob(i: int):
            if i >= len(nums):
                return 0
            return max(rob(i + 1), nums[i] + rob(i + 2))
        
        return rob(0)

    def rob(self, nums: List[int]) -> int:

        memo = [-1] * len(nums)

        def rob(i: int):
            if i >= len(nums): return 0
            if memo[i] != -1: return memo[i]
            memo[i] = max(rob(i + 1), nums[i] + rob(i + 2))
            return memo[i]
            
        return rob(0)