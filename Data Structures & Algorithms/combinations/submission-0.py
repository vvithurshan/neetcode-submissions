class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        sub = []
        nums = list(range(1, n + 1))


        def dfs(i):
            if k == len(sub): # I used i == k instead of k == len(sub)
                res.append(sub[::])
                return

            for j in range(i, len(nums)):
                sub.append(nums[j]) # I used i here instead of j
                dfs(j + 1) # instead of putting j + 1, I used i + 1 second time doing this
                sub.pop()

            return
        dfs(0)

        return res