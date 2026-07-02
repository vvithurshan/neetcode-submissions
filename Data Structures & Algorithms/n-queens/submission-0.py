# Next trial based on the feedback

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        taken = []
        takenCols = set()
        diagleft = set()
        diagright = set()
        rows, cols = n , n 

        def dfs(i,):

            if len(taken) == n:
                print(taken)
                res.append(taken[::]) 
                return

            if i == n:
                return

            for c in range(n):

                if (c in takenCols or
                    (i - c) in diagleft or
                    (i + c) in diagright):
                    continue

                taken.append((i, c))                    
                takenCols.add(c)
                diagleft.add(i - c)
                diagright.add(i + c)

                dfs(i + 1,)

                taken.pop()
                takenCols.remove(c)
                diagleft.remove(i - c)
                diagright.remove(i + c)
            return
                    
        dfs(0,)

        ans = []
        print(f"Result:  {res}")
        for b in res:
            # r = ["."] * n
            # board = [['.' * n] for _ in range(n)]
            board = [['.'] * n for _ in range(n)] 

            for r, c in b:
                board[r][c] = "Q"

            board = ["".join(r) for r in board]
            ans.append(board)

        return ans