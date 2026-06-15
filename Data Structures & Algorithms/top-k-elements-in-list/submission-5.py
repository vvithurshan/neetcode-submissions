class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1


        ans = []

        for key, val in d.items():
            ans.append((key, val))


        ans.sort(key = lambda x : x[-1], reverse=True)

        res = []
        for i in range(k):
            res.append(ans[i][0])

        return res