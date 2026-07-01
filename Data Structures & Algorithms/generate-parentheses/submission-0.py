class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(i, sub, open, close, total):
            
            if open + close == 2 * n:
                ans = "".join(sub)
                if ans:
                    res.append(ans)
                return

            if i == 2 * n:
                return

            if open < n:
                sub.append("(")
                open += 1
                total += 1


                dfs(i + 1, sub, open, close, total)

            
                if sub.pop() == "(":
                    open -= 1

                else:
                    close -= 1

            if open > close:
                sub.append(")")
                close += 1
                total += 1

                dfs(i + 1, sub, open, close, total)

                sub.pop()
                close -= 1

            return

        dfs(0, [], 0, 0, 0)

        return res