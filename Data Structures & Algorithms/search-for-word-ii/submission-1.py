class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.index = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        self.root = TrieNode()

        # Adding words to the trie
        for i in range(len(words)):
            cur = self.root # I did not use this inside the loop
            for c in words[i]:
                if c not in cur.children:
                    cur.children[c] = TrieNode() # I used cur.children = TriNode()
                cur = cur.children[c]
            cur.end = True
            cur.index = i  


        row, col = len(board), len(board[0])
        seen = set()
        res = []

        def dfs(i, j, cur):


            if i < 0 or i >= row or j < 0 or j >= col:
                return

            if (i, j) in seen:
                return

            c = board[i][j]
            if c not in cur.children:
                return False

            cur = cur.children[c]

            if cur.end  and cur.index is not None:
                res.append(words[cur.index ])
                cur.index = None
                # return
            
            seen.add((i, j))
            dfs(i + 1, j, cur)
            dfs(i, j + 1, cur)
            dfs(i - 1, j, cur)
            dfs(i, j - 1, cur)
            seen.remove((i, j))

            return 

        for i in range(row):
            for j in range(col):
                dfs(i, j, self.root)

        return res

            