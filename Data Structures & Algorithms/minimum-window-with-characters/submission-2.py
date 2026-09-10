class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def index(c: str): return ord(c) - ord('A')

        if len(t) > len(s): return ""

        need = [0] * 58
        have = [0] * 58
        left = 0
        covered = 0
        res = ""
        min_subs_len = float('inf')

        for c in t: need[index(c)] += 1
        for i in range(len(t)): have[index(s[i])] += 1
        for i in range(58):
            if have[i] >= need[i]: covered += 1
        if covered == 58: return s[:len(t)];
        
        for right in range(len(t), len(s)):
            i = index(s[right])
            have[i] += 1
            if have[i] == need[i]: covered += 1
            
            while covered == 58:
                if right - left + 1 < min_subs_len:
                    res = s[left : right + 1]
                    min_subs_len = len(res)
                i = index(s[left])
                have[i] -= 1
                if have[i] < need[i]: covered -= 1
                left += 1

        return res
