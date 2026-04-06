class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            d[n] = i
        
        for i, n in enumerate(nums):
            pair = target - n
            if pair in d:
                j = d[pair]
                if i != j: return [min(i, j), max(i, j)]
        
