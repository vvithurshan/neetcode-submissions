class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # 1 2 3 4 

        if nums[0] < nums[-1]:
            return nums[0]

        # 3 4 5 1 2

        l, r = 0, len(nums) - 1

        while l < r:

            mid = l + (r - l)//2
            
            if nums[mid] < nums[r]:

                r = mid

            else:
                l = mid + 1

        return nums[l]
