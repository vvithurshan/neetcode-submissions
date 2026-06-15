class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        bucket = [[] for _ in range(len(nums)+1)]

        for key, val in count.items():
            bucket[val].append(key)

        ans = []
        for i in range(len(nums), 0, -1):
            while len(ans) < k and bucket[i]:
                ans.append(bucket[i].pop()) 
            if len(ans) == k:
                return ans
            