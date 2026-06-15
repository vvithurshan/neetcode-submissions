class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minSofar, maxSofar, res = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            if num < 0:
                minSofar, maxSofar = maxSofar, minSofar
            
            maxSofar = max(maxSofar * num, num)
            minSofar = min(minSofar * num, num)
            res = max(res, maxSofar)
        return res