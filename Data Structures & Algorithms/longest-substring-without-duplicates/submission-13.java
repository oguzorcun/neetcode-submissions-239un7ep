class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        Map<Character, Integer> charIndices = new HashMap();
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            Character c = s.charAt(right);

            // when to shrink
            if (charIndices.containsKey(c) && charIndices.get(c) >= left) {
                left = charIndices.get(c) + 1;
            }

            maxLen = Math.max(maxLen, right - left + 1);
            charIndices.put(c, right);
        }

        return maxLen;
    }
}
