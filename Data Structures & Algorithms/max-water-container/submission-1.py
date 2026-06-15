class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        level = 0

        while l < r:
            current = min(heights[l], heights[r]) * (r - l)
            level = max(level, current)

            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1

        return level