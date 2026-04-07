class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productAll = 1
        zeros = 0
        zero_i = -1
        res = []

        for i, n in enumerate(nums): 
            if n != 0: 
                productAll *= n
            else:
                zero_i = i
                zeros += 1
                if zeros > 1:
                    return [0 for _ in range(len(nums))]
        
        if zeros == 1:
            res = [0 for _ in range(len(nums))]   
            res[zero_i] = productAll 
            return res
        
        for n in nums: 
            res.append(productAll // n)

        return res