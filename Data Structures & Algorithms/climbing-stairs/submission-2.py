class Solution:
    def climbStairs(self, n: int) -> int:
        waysToThePreviousStep = waysToTheStepBeforeThePrevious = 1

        for i in range(n - 1):
            tmp = waysToThePreviousStep
            waysToThePreviousStep = waysToTheStepBeforeThePrevious
            waysToTheStepBeforeThePrevious = tmp + waysToTheStepBeforeThePrevious
        
        return waysToTheStepBeforeThePrevious
