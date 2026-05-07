from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        
        def decodes(code: str) -> bool:
            return len(code) > 0 and code[0] != '0' and 0 < int(code) < 27

        @lru_cache(maxsize=None)
        def rec(i) -> int:
            if i == -1: return 1
            elif i == 0:
                return 1 if decodes(s[0]) else 0

            single = double = 0
            if decodes(s[i]): single = rec(i-1)
            if decodes(s[i-1:i+1]): double = rec(i-2)

            return single + double

        return rec(len(s) - 1)        
            

