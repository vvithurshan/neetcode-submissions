class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check each row


        for row in board:
            seen = set()
            for r in row:
                if r == ".":
                    continue

                if r in seen:
                    return False

                seen.add(r)

        # check each col


        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]

                if val == ".": continue

                if val in seen: return False

                seen.add(val)

        # each box

        for square in range(9):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = (square // 3) * 3 + r # 8 // 3 * 3 + 0
                    col = (square % 3) * 3 + c  # 8 % 3 * 3 + 0

                    val = board[row][col]

                    if val == ".": continue

                    if val in seen: return False

                    seen.add(val)

        return True


