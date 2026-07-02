class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        rows, cols = len(board), len(board[0])

        def dfs(i, j, k):
            
            if len(word) == k:
                return True


            if (i < 0 or i >= rows or j < 0 or j >= cols):
                return False

            if (i, j) in visited:
                return False

            if word[k] != board[i][j]:
                return False

            # append
            visited.add((i, j))
            res = (
                dfs(i + 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j - 1, k + 1)
            )

            visited.remove((i, j))

            return res


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False