class Solution:
    def longest_palindrome_two_pointers(self, s: str) -> str:

        longest_pal = ""
        n = len(s)

        def expand(l: int, r: int):
            nonlocal longest_pal
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > len(longest_pal): 
                    longest_pal = s[l:r + 1]
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)
        for i in range(0, n - 1):
            expand(i, i + 1)
            
        return longest_pal

    def longest_palindrome_dp(self, s: str) -> str:

        longest_pal = ""
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j - i <= 2 and s[i] == s[j]:
                    is_pal[i][j] = True
                else:
                    is_pal[i][j] = s[i] == s[j] and is_pal[i + 1][j - 1]

                if j - i + 1 > len(longest_pal) and is_pal[i][j]:
                    longest_pal = s[i:j + 1]                
                

        return longest_pal

    def longestPalindrome(self, s: str) -> str:
        return self.longest_palindrome_dp(s)