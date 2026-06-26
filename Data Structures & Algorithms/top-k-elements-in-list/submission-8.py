from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        h = []

        for value, freq in count.items():

            heapq.heappush(h, (freq, value))

            if len(h) > k:
                heapq.heappop(h)

        ans = []

        for i in range(k):
            ans.append(h[i][1])

        return ans
        
