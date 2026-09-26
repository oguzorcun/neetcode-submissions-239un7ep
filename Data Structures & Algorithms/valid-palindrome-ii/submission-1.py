class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(t: str) -> bool:
            l, r = 0, len(t) - 1
            while l < len(t) and r > 0:
                if t[l] != t[r]: return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        
        while l < len(s) and r > 0:
            if s[l] != s[r]: return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
            l += 1
            r -= 1
        return True