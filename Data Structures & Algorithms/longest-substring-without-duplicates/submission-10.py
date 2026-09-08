class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            # current char
            c = s[right]

            # if current char has been seen before and it is in the current window (left, right), cut that char and all before it out of the window
            if c in chars and chars[c] >= left:
                left = chars[c] + 1 

            # update max len with unique chars    
            max_length = max(max_length, right - left + 1)

            # save location of current char
            chars[c] = right

        return max_length