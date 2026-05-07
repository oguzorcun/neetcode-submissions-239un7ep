from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        
        def decodes(code: str) -> bool:
            return code[0] != '0' and 0 < int(code) < 27

        @lru_cache(maxsize=None)
        def rec(i) -> int:
            if i == -1: return 1
            elif i == 0: return 1 if decodes(s[0]) else 0

            ways = 0
            if decodes(s[i]): ways += rec(i-1)
            if decodes(s[i-1:i+1]): ways += rec(i-2)

            return ways

        return rec(len(s) - 1)        
            

