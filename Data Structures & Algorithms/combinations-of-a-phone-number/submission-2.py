class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        res = []
        n = len(digits)
        sub = []

        numToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):

            if i == n:
                ans = "".join(sub)
                res.append(ans)
                return

            
            for c in numToChar[digits[i]]:
                sub.append(c)

                dfs(i + 1)

                sub.pop()

            return

        dfs(0)

        return res