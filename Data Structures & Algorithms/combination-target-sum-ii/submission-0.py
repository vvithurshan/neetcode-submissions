class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        d = {}
        res = []
        def dfs(i, cur, total):
            if total == target:
                # res.append(cur.copy())
                d["".join(sorted(cur))] = 0
                return
            if i >= len(nums) or total > target:
                return 
            cur.append(str(nums[i]))
            dfs(i + 1, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)

        for subset in d:
            temp = [int(i) for i in list(subset)]
            res.append(temp)
        return res