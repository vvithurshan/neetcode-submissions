from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == ".": continue

                row = val in rows[r]
                col = val in cols[c]
                square = val in squares[(r // 3, c // 3)]

                if row or col or square: return False

                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True