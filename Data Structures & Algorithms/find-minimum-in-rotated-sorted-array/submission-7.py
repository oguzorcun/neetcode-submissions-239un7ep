class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]
        
        left, right, mid = 0, len(nums) - 1, len(nums) // 2

        while left <= right:
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[left] > nums[mid]:
                right = mid
            elif nums[right] < nums[mid]:
                left = mid
            # else:
            #     return nums[0]

            mid = (left + right + 1) // 2