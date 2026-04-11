class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxWater = 0

        while i < j:
            floor, left, right = j - i, heights[i], heights[j]
            water = min(left, right) * floor
            maxWater = max(water, maxWater)
            if left < right:
                i += 1
            else:
                j -= 1
        return maxWater