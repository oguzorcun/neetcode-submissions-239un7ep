class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def combine(comb: List[int], cur: int):
            res.append(comb.copy())
            for i in range(cur, len(nums)):
                comb.append(nums[i])
                combine(comb, i + 1)
                comb.pop()
            return

        combine([], 0)    
        return res