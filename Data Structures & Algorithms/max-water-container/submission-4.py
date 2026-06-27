class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxW = 0

        l, r = 0, len(heights) - 1 # I did not use - 1

        while l < r:

            water = min(heights[l], heights[r]) * (r - l)

            maxW = max(water, maxW)

            if heights[l] <= heights[r]:
                l += 1

            else:
                r -= 1

        return maxW