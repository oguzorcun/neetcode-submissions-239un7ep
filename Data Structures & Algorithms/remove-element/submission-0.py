class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        match = 0
        for i, n in enumerate(nums):
            if n == val: 
                nums[i] = 101
                match += 1

        k = len(nums) - match
        nums.sort()
        print(nums)

        return k
