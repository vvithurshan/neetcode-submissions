from heapq import heappop, heappush, heapify

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxh = []
        heapify(maxh)

        for num in nums:
            heappush(maxh, num)
            if len(maxh) > k:
                heappop(maxh)

        return maxh[-k]