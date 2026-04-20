class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_chars = defaultdict(int)
        for c in t: t_chars[c] += 1
        chars = defaultdict(int)
        l = 0
        res = ""
        len_res = float('inf')

        for r, c in enumerate(s):
            if c in t_chars:
                chars[c] += 1
            
            while all(chars[c] >= t_chars[c] for c in t_chars.keys()):
                if r - l + 1 < len_res:
                    res = s[l:r+1]
                    len_res = len(res)
                if s[l] in chars: chars[s[l]] -= 1
                l += 1

        return res
