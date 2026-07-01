# Cleanest approach 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def dfs(open_count, close_count, path):
            # Base case:
            # We've used all n opening and n closing parentheses.
            if open_count == close_count == n:
                res.append("".join(path))
                return

            # Choice 1: Add an opening parenthesis.
            # We can do this only if we haven't used all n opening parentheses.
            if open_count < n:
                path.append("(")
                dfs(open_count + 1, close_count, path)
                path.pop()                    # Backtrack

            # Choice 2: Add a closing parenthesis.
            # We can do this only if there are unmatched '(' available.
            if close_count < open_count:
                path.append(")")
                dfs(open_count, close_count + 1, path)
                path.pop()                    # Backtrack

        dfs(0, 0, [])

        return res