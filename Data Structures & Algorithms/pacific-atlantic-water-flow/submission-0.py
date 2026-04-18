class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def flows(r: int, c: int, visited: set):
            visited.add((r, c))
            for dr, dc in dirs:
                fr, fc = r + dr, c + dc
                if ( 0 <= fr < rows and 0 <= fc < cols
                    and (fr, fc) not in visited
                    and heights[fr][fc] >= heights[r][c]
                ):
                    flows(fr, fc, visited)
            
        atlantic, pacific = set(), set()

        for r in range(rows):
            flows(r, 0, pacific)
            flows(r, cols - 1, atlantic)


        for c in range(cols):
            flows(0, c, pacific)
            flows(rows - 1, c, atlantic)

        return list(atlantic & pacific)