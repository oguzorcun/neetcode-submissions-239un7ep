class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        max_len = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_frequency = max(count.values())
            
            if r - left - max_frequency + 1 > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, r - left + 1)

        return max_len