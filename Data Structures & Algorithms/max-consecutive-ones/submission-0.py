class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = maxval = 0

        for n in nums:
            if n == 1:
                cur += 1
                maxval = max(maxval, cur)
            else:
                cur = 0

        return maxval