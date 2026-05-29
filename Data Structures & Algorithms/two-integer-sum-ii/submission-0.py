class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            pair = target - numbers[i]
            while pair <= numbers[j]:
                if pair == numbers[j]: return [i+1, j+1]
                j -= 1
            i += 1
            