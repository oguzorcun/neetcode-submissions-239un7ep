class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islandCnt = 0

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if grid[r][c] == '0':
                return

            grid[r][c] = '0'
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islandCnt += 1
                    dfs(r, c)
        
        return islandCnt