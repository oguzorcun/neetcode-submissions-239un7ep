class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        max_len = 0
        count_most_frequent_char = 0
        count = defaultdict(int)

        for right, c in enumerate(s):
            count[c] += 1
            current_window_size = right - left + 1
            count_most_frequent_char = max(count_most_frequent_char, count[c])
            
            count_chars_that_need_to_be_replaced = current_window_size - count_most_frequent_char 
            if count_chars_that_need_to_be_replaced > k:
                # shrink the window from left by 1
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

        