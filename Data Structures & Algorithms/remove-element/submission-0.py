class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 1

        while i < len(nums) and j < len(nums):
            while i < len(nums) and nums[i] != val:
                i += 1
                j += 1

            while j < len(nums) and nums[j] == val:
                j += 1

            if i < len(nums) and j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1

        return i