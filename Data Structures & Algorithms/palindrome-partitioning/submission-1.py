class Solution:
    def isPalindrome(self, s, i, j):

        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        sub = []

        def backtrack(i):
            if i >= n:
                res.append(sub[::]) # I did not use [::]
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    sub.append(s[i:j+1])
                    backtrack(j + 1) # I put i previously
                    sub.pop()

            return

        backtrack(0)

        return res