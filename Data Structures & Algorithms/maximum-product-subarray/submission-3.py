class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = max_prod = 1
        res = nums[0]
        
        for i in range(len(nums)):
            max_prod, min_prod = max(nums[i], min_prod * nums[i], max_prod * nums[i]), min(nums[i], min_prod * nums[i], max_prod * nums[i])
            res = max(max_prod, res)
        return res