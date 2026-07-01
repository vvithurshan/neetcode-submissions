class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []

        def dfs(i, sub, total):

            # make sure you check the target first 
            if total == target:
                res.append(sub.copy())
                return

            if total > target or i >= len(candidates):
                return

            sub.append(candidates[i])
   
            dfs(i + 1, sub, total + candidates[i])

            sub.pop()

            # I do not want to start from the current element
            # but if the next element is the same as the current element
            # I will again start from the current element
            while i + 1 < len(candidates) and \
                candidates[i] == candidates[i + 1]:
                i += 1
                
            dfs(i + 1, sub, total)

            return

        dfs(0, [], 0)
        return res
