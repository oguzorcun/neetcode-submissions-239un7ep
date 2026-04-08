class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in s:
                start, l = n, 1
                while start+1 in s:
                    l += 1
                    start += 1
                longest = max(l, longest)
        return longest
