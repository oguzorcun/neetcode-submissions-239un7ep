class Solution {
    private int[] nums;

    public int[] sortArray(int[] nums) {
        this.nums = nums;
        this.mergeSort(0, nums.length - 1);
        return nums;
    }

    private void mergeSort(int L, int R) {
        if (L >= R) return;

        int M = (L + R) / 2;
        this.mergeSort(L, M);        
        this.mergeSort(M + 1, R);
        this.merge(L, M, R);
    }

    private void merge(int L, int M, int R) {
        ArrayList<Integer> tmp = new ArrayList<>();
        int i = L;
        int j = M + 1;

        while (i <= M && j <= R) {
            if (nums[i] <= nums[j]) {
                tmp.add(nums[i++]);
            } else {
                tmp.add(nums[j++]);
            }
        }
        while (i <= M) {
            tmp.add(nums[i++]);
        }
        while (j <= R) {
            tmp.add(nums[j++]);
        }

        // put the sorted segment back in the original arr
        for (i = L; i <= R; i++) {
            nums[i] = tmp.get(i - L);
        }
    }
}