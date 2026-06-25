class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        l, r = 1, len(nums) - 1

        while l <= r:

            mid = l + (r - l)//2

            lessOrEqual = sum(1 for num in nums if num <= mid)

            if lessOrEqual <= mid:
                l = mid + 1

            else:
                r = mid - 1

        return l