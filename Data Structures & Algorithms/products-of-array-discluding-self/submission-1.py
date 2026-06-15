class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zeros = {}

        prod = 1

        for i in range(len(nums)):
            if nums[i]:
                prod *= nums[i]
            else:
                zeros[i] = 1

        if len(zeros) > 1:
            return [0] * len(nums)

        if zeros:
            ans = [0] * len(nums)
            ans[list(zeros.keys())[0]] = prod
            return ans

        ans = [0] * len(nums)

        for i in range(len(nums)):

            ans[i] = prod//nums[i]

        return ans
