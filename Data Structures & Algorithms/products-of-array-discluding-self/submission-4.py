class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1

        zero = []

        for i, num in enumerate(nums):
            if num == 0:
                zero.append(i)

                if len(zero) > 1:
                    return [0] * len(nums)
            else:                           # mistake I forgot to add the else 
                prod *= num

        ans = [0] * len(nums)

        if zero:
            ans[zero[0]] = prod

            return ans

        for i, num in enumerate(nums):

            ans[i] = prod // num

        return ans