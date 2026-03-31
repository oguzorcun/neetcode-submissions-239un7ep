class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: # there cannot be any value that will make the sum 0 after this point as the list is sorted. all items are positive
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: 
                        # ['-1', '0', 0, 1, '1', -1, -1] there is no need to check for a duplicate on RHS too because changing only left guaranties a unique next triplet
                        l += 1
                        
        return res