class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        n = len(candidates)
        res = []
        sub = []
        total = 0

        def backtrack(i, total):
            
            if total == target:
                res.append(sub[::])
                return

            if total > target:
                return

            if i == n:
                return

            sub.append(candidates[i])

            backtrack(i + 1, total + candidates[i])

            while  i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1

            sub.pop()

            backtrack(i + 1, total)

        backtrack(0, 0)

        return res
            
