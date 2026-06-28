# June 28

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        res = 0

        for i in range(32):
            
            mask = 1 << i

            x = 0
            for num in nums:
                if num & mask:
                    x += 1


            y = 0
            for num in range(1, len(nums)):
                if num & mask:
                    y += 1

            if x > y:
                res |= mask

        return res