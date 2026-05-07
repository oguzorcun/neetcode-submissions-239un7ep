class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        pal_count = 0
        is_pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
                    pal_count += 1

        return pal_count