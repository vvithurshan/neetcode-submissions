class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        grid = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    if val not in row:
                        row.add(val)
                    else:
                        return False
                    r = i // 3
                    c = j // 3
                    if val not in grid[r][c]:
                        grid[r][c].add(val)
                    else:
                        return False
                val = board[j][i]
                if val != ".":
                    if val not in col:
                        col.add(val)
                    else:
                        return False
        return True
