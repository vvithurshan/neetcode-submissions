class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for i in range(len(nums)):

            bal = target - nums[i]

            if bal in d:
                return [d[bal], i]
            
            d[nums[i]] = i