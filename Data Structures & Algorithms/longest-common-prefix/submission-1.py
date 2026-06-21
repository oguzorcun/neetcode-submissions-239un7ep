class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 200
        prefix = ""

        for s in strs: min_len = min(min_len, len(s))

        for j in range(min_len):
            c = strs[0][j]
            i = 1
            while i < len(strs):
                if strs[i][j] != c: break
                i += 1
            if i < len(strs): break
            prefix += c
        
        return prefix
            

