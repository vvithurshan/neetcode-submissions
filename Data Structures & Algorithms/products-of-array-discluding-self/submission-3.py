class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        cnt_zero = 0
        prod = 1
        pos_zero = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                cnt_zero += 1
                pos_zero = i

                if cnt_zero > 1:
                    return [0] * len(nums)
                continue

            prod *= nums[i]


        if cnt_zero :
            res = [0] * len(nums)
            res[pos_zero] = prod
            return res


        res = []

        # do not have any zeros
        for i in range(len(nums)):

            res.append(prod//nums[i])

        return res
                