class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        cache = {}
        n = len(s)

        def backtrack(i):
            
            if i == n:
                return [""]

            if i in cache:
                return cache[i]

            res = []
            for j in range(i, n):
                word = s[i : j + 1]
                
                if word not in wordDict:
                    continue

                strings = backtrack(j + 1)

                for substr in strings:
                    sentence = word
                    if substr:
                        sentence += " " + substr

                    res.append(sentence)

            cache[i] = res

            return res

        return backtrack(0)

