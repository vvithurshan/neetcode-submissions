class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        subset = []


        def dfs(i):
            if i >= n:
                res.append(subset.copy())
                return

            # Decision to add
            subset.append(nums[i])
            dfs(i + 1)

            # Decision to Not add
            subset.pop()
            dfs(i + 1)

            return 

        dfs(0)

        return res