from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        maj = (1, nums[0])
        cnt = defaultdict(int)

        for num in nums:
            cnt[num] += 1
            maj = max(maj, (cnt[num], num))

        return maj[-1]