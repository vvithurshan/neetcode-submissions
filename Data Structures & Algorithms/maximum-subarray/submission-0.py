class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, maxSofar = nums[0], 0
        for num in nums:
            if maxSofar < 0:
                maxSofar = 0
            maxSofar = maxSofar + num
            maxSum = max(maxSum, maxSofar)

        return maxSum