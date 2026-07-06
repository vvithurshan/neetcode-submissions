class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        positions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.maxArea = 0

        def dfs(r, c, area):

            if r < 0 or r >= rows or \
                c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            area = 0

            for dr, dc in positions:

                area += dfs(r + dr, c + dc, area  + 1)

            return area + 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.maxArea = max(self.maxArea, dfs(r, c, 0))

        return self.maxArea
