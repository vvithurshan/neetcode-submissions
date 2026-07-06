from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])       
        island = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


        def bfs(r, c):

            dq = deque()
            dq.append((r, c))

            while dq:

                r, c = dq.popleft()
                
                for dr, dc in directions:
                    dr, dc = r + dr, c + dc

                    if dr < 0 or dr >= rows or \
                        dc < 0 or dc >= cols or \
                        grid[dr][dc] == "0":
                        continue

                    grid[dr][dc] = "0"

                    dq.append((dr, dc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    island += 1

        return island