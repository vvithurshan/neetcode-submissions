class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        level = 0

        while l < r:
            curr = min(heights[l], heights[r]) * (r-l)
            level = max(curr, level)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return level