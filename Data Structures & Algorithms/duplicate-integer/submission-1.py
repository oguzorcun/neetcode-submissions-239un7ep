class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set()

        for n in nums:
            if n in d:
                return True
            d.add(n)
        
        return False