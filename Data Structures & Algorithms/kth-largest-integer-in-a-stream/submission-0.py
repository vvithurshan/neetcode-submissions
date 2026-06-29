import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.h = []

        for num in nums:
            heapq.heappush(self.h, -num)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.h, -val)
        
        top = heapq.nsmallest(self.k, self.h)

        return -top[-1]