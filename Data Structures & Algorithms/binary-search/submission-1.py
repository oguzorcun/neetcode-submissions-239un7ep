class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while r >= l:
            i = (r + l) // 2
            if nums[i] == target:
                return i
            elif target > nums[i]:
                l = i + 1
            else:
                r = i - 1
        return -1