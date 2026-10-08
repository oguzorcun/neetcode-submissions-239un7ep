class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]


        # if len(nums) == 1:
        #     return nums[0]

        # if nums[0] < nums[-1]:
        #     return nums[0]
        
        # left, right = 0, len(nums) - 1

        # while left < right:
        #     mid = (left + right) // 2

        #     if nums[mid] > nums[mid + 1]:
        #         return nums[mid + 1]
        #     if nums[left] > nums[mid]:
        #         right = mid
        #     else:
        #         left = mid