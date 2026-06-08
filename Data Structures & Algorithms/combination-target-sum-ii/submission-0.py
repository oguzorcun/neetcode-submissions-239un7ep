class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def checksum(comb: List[int], comb_sum: int, left: int):
            if comb_sum == target:
                res.append(comb.copy())
                return

            for i in range(left, len(candidates)):
                if i > left and candidates[i - 1] == candidates[i]: continue
                if comb_sum + candidates[i] <= target:
                    comb_sum += candidates[i]
                    comb.append(candidates[i])
                    checksum(comb, comb_sum, i + 1)
                    comb_sum -= candidates[i]
                    comb.pop()
        
        checksum([], 0, 0)
        return res