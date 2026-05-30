class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars_needed = defaultdict(int)
        i = j = 0
        for c in s1: chars_needed[c] += 1

        while i < len(s2):
            j = i
            chars_found = defaultdict(int)
            found = 0
            while j < len(s2) and s2[j] in chars_needed:
                chars_found[s2[j]] += 1
                if chars_found[s2[j]] > chars_needed[s2[j]]: break
                if chars_found[s2[j]] == chars_needed[s2[j]]: found += 1
                if found == len(chars_needed): return True
                j += 1
            i += 1
                
        return False