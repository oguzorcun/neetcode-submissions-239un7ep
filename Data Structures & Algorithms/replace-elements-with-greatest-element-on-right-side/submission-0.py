class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            arr[i], max_val = max_val, max(max_val, arr[i])

            # tmp = arr[i]
            # arr[i] = max_val
            # max_val = max(max_val, tmp)

        return arr