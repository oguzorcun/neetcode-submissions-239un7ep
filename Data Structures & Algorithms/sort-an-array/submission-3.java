class Solution {
    private int[] nums;
    private int[] tmp;
    public int[] sortArray(int[] nums) {
        this.nums = nums;
        this.tmp = new int[nums.length];

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
        System.arraycopy(nums, L, tmp, L, R - L + 1);
        int i = L;
        int j = M + 1;
        int k = L;

        while (i <= M && j <= R) {
            if (tmp[i] <= tmp[j]) {
                nums[k] = tmp[i];
                i += 1;
                k += 1;
            } else {
                nums[k] = tmp[j];
                j += 1;
                k += 1;
            }
        }
        while (i <= M) {
            nums[k] = tmp[i];
            i += 1;
            k += 1;
        }
        while (j <= R) {
            nums[k] = tmp[j];
            j += 1;
            k += 1;
        }
    }
}