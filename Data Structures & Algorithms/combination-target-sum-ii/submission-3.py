class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        sub = []
        total = 0

        def dfs(i):
            nonlocal total
            if total == target:
                res.append(sub.copy())
                return

            if total > target or i >= len(candidates):
                return

            sub.append(candidates[i])
            total += candidates[i]
            dfs(i + 1)

            sub.pop()
            total -= candidates[i]

            while i + 1 < len(candidates) and \
                candidates[i] == candidates[i + 1]:
                i += 1
                
            dfs(i + 1)

            return

        dfs(0)
        return res
