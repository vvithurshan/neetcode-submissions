from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        ans = set()
        cnt = defaultdict(int)
        t = len(nums)/3

        for num in nums:
            cnt[num] += 1
            if cnt[num] > t:
                ans.add(num)

        return list(ans)