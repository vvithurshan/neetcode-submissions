# I derived most the parts
# But corrected with ChatGPT
# Good Job

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(i, j, k):
            if k >= len(word):
                return True
                
            if i >= rows or i < 0 or j >= cols or j < 0:
                return False

            if (i, j) in visited:
                return False

            if board[i][j] != word[k]:
                return False

            visited.add((i, j))
            res = (
                dfs(i + 1, j, k + 1) or 
             
                dfs(i, j + 1, k + 1) or 
 
                dfs(i - 1, j, k + 1) or 

                dfs(i, j - 1, k + 1) )

            visited.remove((i, j))

            return res
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False
        