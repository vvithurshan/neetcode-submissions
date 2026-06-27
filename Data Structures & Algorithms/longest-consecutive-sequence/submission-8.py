class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        longest = 0

        sets = sorted(set(nums))

        i, j = 0, 0
        long = 0
        n = len(sets)

        while j < n:
            if sets[j] == (sets[i] + long):
                long += 1
                j += 1
                longest = max(longest, long)

            else:
                long = 0
                i = j


        return longest