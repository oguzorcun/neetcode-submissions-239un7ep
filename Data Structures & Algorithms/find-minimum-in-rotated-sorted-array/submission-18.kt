class Solution {
    fun findMin(nums: IntArray): Int {

        var l = 0
        var r = nums.size - 1

        if (nums[l] < nums[r] || r == 0) return nums[0]

        while (l < r) {
            var mid = (l + r) / 2
            if (nums[mid] > nums[mid + 1])
                return nums[mid + 1]
            if (nums[l] < nums[mid]) 
                l = mid
            else r = mid

        }
        return -1
    }
}
