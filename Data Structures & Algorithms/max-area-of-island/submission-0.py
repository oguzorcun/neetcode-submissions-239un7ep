class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def area(r: int, c: int) -> int:
            if not 0 <= r < rows or not 0 <= c < cols: return 0
            if grid[r][c] == 0: return 0

            grid[r][c] = 0

            return ( 1 + 
                area(r, c + 1) +
                area(r, c - 1) +
                area(r + 1, c) +
                area(r - 1, c)
            )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    max_area = max(max_area, area(r, c))

        return max_area