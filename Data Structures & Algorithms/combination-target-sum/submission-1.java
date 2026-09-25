class Solution {

    private void discover(int[] nums, List<Integer> comb, int comb_sum, int cursor, List<List<Integer>> res, int target) {
        if (comb_sum == target) { 
            res.add(new ArrayList(comb));
            return;
        }

        for(int i = cursor; i < nums.length; i++) {
            if (comb_sum + nums[i] <= target) {
                comb_sum += nums[i];
                comb.add(nums[i]);
                discover(nums, comb, comb_sum, i, res, target);
                comb_sum -= nums[i];
                comb.removeLast();
            }
        }
    }

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        
        List<List<Integer>> res = new ArrayList();

        discover(nums, new ArrayList(), 0, 0, res, target);

        return res;
    }
}
