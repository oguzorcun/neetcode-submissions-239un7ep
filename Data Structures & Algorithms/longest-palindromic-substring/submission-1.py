class Solution:
    def longestPalindrome(self, s: str) -> str:

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