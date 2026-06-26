from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        ans = []

        for key, val in count.items():
            ans.append((val, key))    


        ans.sort(reverse=True)
        res = []

        for i in range(k):
            res.append(ans[i][1])


        return res

        