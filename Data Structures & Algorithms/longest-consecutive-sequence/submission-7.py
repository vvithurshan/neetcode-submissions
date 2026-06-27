class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        sets = set(nums)

        for num in sets:
            if num - 1 in sets: continue

            length = 0
            while num in sets:
                length += 1
                num += 1

            longest = max(longest, length)

        return longest 