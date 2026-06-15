class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(nums[i], 0, -1):
                if i + j >= len(nums):
                    continue
                dp[i] = dp[i + j]
                if dp[i]:
                    break
        return dp[0]