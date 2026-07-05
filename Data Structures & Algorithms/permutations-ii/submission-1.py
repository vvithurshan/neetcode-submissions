class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        taken = [False] * n
        res = []
        perm = []
        nums.sort()

        def dfs():
            if len(perm) == n:
                res.append(perm[::])
                return

            for i in range(n):

                if i > 0 and nums[i - 1] == nums[i] and \
                    not taken[i - 1]:
                    continue

                if taken[i]:
                    continue

                taken[i] = True

                perm.append(nums[i])

                dfs()

                perm.pop()

                taken[i] = False

        dfs()

        return res