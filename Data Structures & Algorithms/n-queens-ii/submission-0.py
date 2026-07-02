class Solution:
    def totalNQueens(self, n: int) -> int:
        
        self.res =  0 # I did not use self.res before, just res
        sub = []
        TakenCols = set()
        Diagleft = set()
        Diagright = set()

        def dfs(r):
            if len(sub) == n:
                self.res += 1
                return

            if r == n:
                return

            for c in range(n):
                if (c in TakenCols or
                    (r - c) in Diagleft or
                    (r + c) in Diagright):
                    continue
                sub.append((r, c))
                Diagright.add(r + c)
                TakenCols.add(c)
                Diagleft.add(r - c)
                dfs(r + 1)
                sub.pop()
                TakenCols.remove(c)
                Diagleft.remove(r - c)
                Diagright.remove(r + c)

            return

        dfs(0)

        return self.res