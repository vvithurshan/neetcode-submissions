class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sumsofar = 0
        presum = {0 : 1}

        for num in nums:
            sumsofar += num

            diff = sumsofar - k

            if diff in presum:
                res += presum[diff]

            presum[sumsofar] = presum.get(sumsofar, 0) + 1

        return res