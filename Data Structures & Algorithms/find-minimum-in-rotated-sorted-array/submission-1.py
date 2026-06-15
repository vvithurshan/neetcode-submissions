class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minE = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                minE = min(nums[l], minE)

            mid = (l+r+1)//2
            minE = min(minE, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return minE
         