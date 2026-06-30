class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sub = []
        n = len(nums)

        def dfs(i):
            
            tol = sum(sub)

            if tol == target:
                res.append(sub.copy())
                return

            if tol > target or i >= n:
                return

            sub.append(nums[i])

            dfs(i)

            # sub.pop()

            # dfs(i + 1)

            #
            sub.pop()
            dfs(i + 1)

            return

        dfs(0)
        return res