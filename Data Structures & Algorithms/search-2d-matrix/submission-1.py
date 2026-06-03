class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            mid = (l + r) // 2
            n = matrix[mid // cols][mid % cols]
            if target == n: return True
            if target > n: l = mid + 1
            else: r = mid - 1 
        return False

        # l, r, i = 0, len(matrix) - 1, 0

        # while l <= r:
        #     i = (l + r) // 2
        #     if matrix[i][0] <= target <= matrix[i][-1]: break
        #     elif matrix[i][0] > target: r = i - 1
        #     else: l = i + 1

        # l, r = 0, len(matrix[0]) - 1

        # while l <= r:
        #     j = (l + r) // 2
        #     if matrix[i][j] == target: return True
        #     elif matrix[i][j] > target: r = j - 1
        #     else: l = j + 1
        
        # return False