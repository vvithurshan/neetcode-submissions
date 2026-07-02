class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        res = []
        sub = []
        n = len(s)

        def dfs(i):
            if i == n:
                ans = " ".join(sub)
                res.append(ans)
                return

            for j in range(i, n):
                word = s[i : j + 1]
                if word in wordDict:
                    sub.append(word)
                    dfs(j + 1)
                    sub.pop()

            return

        dfs(0)

        return res

        
