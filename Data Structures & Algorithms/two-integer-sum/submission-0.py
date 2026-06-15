class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in D:
                return [D[tar], i]
            else:
                D[nums[i]] = i
