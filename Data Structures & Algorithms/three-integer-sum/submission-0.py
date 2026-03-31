class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_map = {num: i for i, num in enumerate(nums)}
        triplets = set()

        for i, m in enumerate(nums):
            for j, n in enumerate(nums):
                third = 0 - m - n
                if third in nums_map and len({i, j, nums_map[third]}) == 3:
                    triplets.add(tuple(sorted([n, m, third])))

        return [list(t) for t in triplets]