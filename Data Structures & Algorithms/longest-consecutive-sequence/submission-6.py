class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # 
        if not nums:
            return 0
        
        # remove the duplicates

        sorted_nums = sorted(list(set(nums)))

        long = 0
        longest = 0
        
        i = 0
        j = 1

        # 2, 3, 4, 5, 10, 20, 21, 22, 23, 24

        while j < len(sorted_nums):

            if sorted_nums[i] + 1 == sorted_nums[j]:
                long += 1
                longest = max(longest, long)
                j += 1
                i += 1

            else:
                long = 0
                i = j
                j += 1

        return longest + 1
