from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxArea = 0

        def bfs(r, c):
            
            area = 1
            dq = deque()
            grid[r][c] = 0
            dq.append((r, c))

            while dq:
                r, c = dq.popleft()

                for dr, dc in directions:
                    dr, dc = dr + r, dc + c

                    if dr < 0 or \
                        dc < 0 or dr >= rows or dc >= cols or \
                        grid[dr][dc] == 0:
                        continue
                    
                    area += 1

                    grid[dr][dc] = 0

                    dq.append((dr, dc))

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(bfs(r, c), maxArea)

        return maxArea