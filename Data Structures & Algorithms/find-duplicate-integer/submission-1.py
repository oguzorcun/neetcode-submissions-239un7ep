class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = nums[0]
        for _ in range(len(nums)):
            if nums[i] == 0: return i
            next_i = nums[i]
            nums[i] = 0
            i = next_i
        return 0