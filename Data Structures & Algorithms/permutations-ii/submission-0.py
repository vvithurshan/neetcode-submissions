class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        taken = [False] * n
        res, sub = [], []

        def dfs():
            if len(sub) == n:
                res.append(sub[::])
                return # again, I did not use return

            # if i == n: # I did not add this before
            #     return

            for j in range(n):
                if j > 0 and nums[j] == nums[j - 1] and not taken[j - 1]: # I used taken[j] == taken[j - 1]
                    continue # I used return

                if taken[j]:
                    continue

                taken[j] = True
                sub.append(nums[j])
                dfs()
                sub.pop()
                taken[j] = False
            return

        dfs()

        return res