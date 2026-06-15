class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digittolet = {        
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
            '0': ['+']}

        res = []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digittolet[digits[i]]:
                backtrack(i + 1, curStr + c)
        
        if digits: backtrack(0, "")
        return res
        