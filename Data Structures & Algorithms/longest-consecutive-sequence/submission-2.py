class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest = 0
        longsofar = 0
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                longsofar += 1
                longest = max(longest, longsofar)
            else:
                longsofar = 0

        return longest + 1