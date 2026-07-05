class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)

        def dfs(i):

            if i == n:
                return [[]]

            perms = dfs(i + 1)

            res = []

            for p in perms:

                for j in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(j, nums[i])

                    res.append(p_copy)
            
            return res

        return dfs(0)


                