class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        sub = []

        n = len(s)

        def dfs(i):
            if i == n:
                res.append(sub[::])
                return

            for j in range(i, n):

                if self.palin(s, i, j):

                    w = s[i : j + 1]
                    sub.append(w)
                    dfs(j + 1)

                    sub.pop()

        dfs(0)

        return res

    def palin(self, s, i, j):

        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True