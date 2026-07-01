class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)//2 + 1
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            if count[n] == majority: return n
        return 0

