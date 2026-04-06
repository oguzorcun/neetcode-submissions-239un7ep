class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # def backtrack(state, choices):
        #     if is_solution(state):
        #         result.append(state.copy())  # record answer
        #         return

        #     for choice in choices:
        #         if is_valid(choice, state):
        #             make_choice(state, choice)      # choose
        #             backtrack(state, next_choices)  # explore
        #             undo_choice(state, choice)      # un-choose (backtrack)

        res = []

        def checksum(comb: List[int], sum_comb: int, left: int):
            if sum_comb == target:
                res.append(comb.copy())
                return

            for i in range(left, len(nums)):
                if sum_comb + nums[i] <= target:
                    sum_comb += nums[i]
                    comb.append(nums[i])
                    checksum(comb, sum_comb, i)
                    sum_comb -= nums[i]
                    comb.pop()
        
        checksum([], 0, 0)
        return res
                
                    
