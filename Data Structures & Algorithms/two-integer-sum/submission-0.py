class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                return [mp[nums[i]], i]
            mp[target - nums[i]] = i