class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        seenCols = set()
        seenDiag1 = set()
        seenDiag2 = set()

        board = [["."] * n for _ in range(n)]

        def dfs(r, filled):

            if filled == n:
                ans = ["".join(row) for row in board]                
                res.append(ans[::])

            if r == n:
                return

            for c in range(n):

                if c in seenCols or \
                    (r - c) in seenDiag1 or \
                        (r + c) in seenDiag2:
                            continue

                seenCols.add((c))
                seenDiag1.add((r - c))
                seenDiag2.add((r + c))

                board[r][c] = "Q"

                dfs(r + 1, filled + 1)

                board[r][c] = "."

                seenCols.remove((c))
                seenDiag1.remove((r - c))
                seenDiag2.remove((r + c))


        dfs(0, 0)

        return res