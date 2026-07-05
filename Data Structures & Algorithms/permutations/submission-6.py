
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        taken = [False] * n
        perm = []
        res = []

        def dfs():
            if len(perm) == n:
                res.append(perm[::])
                return
            
            for j in range(n):
                if taken[j]:
                    continue
                
                taken[j] = True
                perm.append(nums[j])

                dfs()

                perm.pop()

                taken[j] = False

        dfs()

        return res