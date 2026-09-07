class Solution {
    public int maxProfit(int[] prices) {

        int left = 0;
        int maxProfit = 0;

        for (int right = 0; right < prices.length; right++) {
            int profit = prices[right] - prices[left];

            // shrink the window if some condition holds
            
            if (prices[right] < prices[left]) {
                left = right;
            }

            maxProfit = Math.max(maxProfit, profit);
        }
        
        return maxProfit;
    }
}
