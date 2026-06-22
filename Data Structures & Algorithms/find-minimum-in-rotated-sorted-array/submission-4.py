class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # 1 2 3 4
        # 3 4 1 2

        l, r = 0, len(nums) - 1

        while l < r:

            m = l + (r - l)//2

            if nums[m] < nums[r]:
                r = m

            else:
                l = m + 1


        return nums[l]


    def findMax(self, nums):

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l)//2

            if nums[m] >= nums[l]:
                l = m

            else:
                r = m - 1


        return nums[l]