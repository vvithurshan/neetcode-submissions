class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp(num):
            r1, r2 = 0, 0

            for i in num:
                temp = max(r1 + i, r2)
                r1 = r2
                r2 = temp
            return r2
        
        return max(dp(nums[1:]), dp(nums[:-1]))