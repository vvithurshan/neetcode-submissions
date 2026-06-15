class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        unique = list(set(nums))
        unique.sort()
        longest = 0
        maxlongest = 0

        for i in range(1, len(unique)):
            if unique[i - 1] == unique[i] - 1:
                longest += 1
                maxlongest = max(maxlongest, longest)

            else:
                longest = 0
        return maxlongest + 1