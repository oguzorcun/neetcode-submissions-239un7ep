class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> count = new HashMap();
        int mostFrequentCharCount = 0;
        int longestRepeatingCharStrLen = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            Character c = s.charAt(right);
            count.put(c, count.getOrDefault(c, 0) + 1);
            mostFrequentCharCount = Math.max(mostFrequentCharCount, count.get(c));

            // shrink baby
            if (right - left + 1 - mostFrequentCharCount > k) {
                // shrink
                count.put(s.charAt(left), count.get(s.charAt(left)) - 1);
                left += 1;
            }

            longestRepeatingCharStrLen = Math.max(longestRepeatingCharStrLen, right - left + 1);
        }
        return longestRepeatingCharStrLen;

    }
}

