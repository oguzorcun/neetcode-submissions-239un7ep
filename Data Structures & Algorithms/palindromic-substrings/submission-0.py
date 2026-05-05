class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        pal_count = 0
        is_pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i <= 2 and s[i] == s[j]:
                    is_pal[i][j] = True
                else:
                    is_pal[i][j] = s[i] == s[j] and is_pal[i + 1][j - 1]
            
                if is_pal[i][j]: pal_count += 1

        return pal_count