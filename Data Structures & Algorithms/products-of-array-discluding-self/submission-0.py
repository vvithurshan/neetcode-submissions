class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = []
        prod = 1

        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                zeros.append(i)
                if len(zeros) == 2:
                    return [0] * len(nums)
        if len(zeros):
            ans = [0] * len(nums)
            ans[zeros[0]] = prod
            return ans
        ans = []
        for num in nums:
            ans.append(prod//num)

        return ans
