class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            c = s[right]
            if c in chars and chars[c] >= left:
                left = chars[c] + 1 
            # else:
            max_length = max(max_length, right - left + 1)
            chars[c] = right

        return max_length