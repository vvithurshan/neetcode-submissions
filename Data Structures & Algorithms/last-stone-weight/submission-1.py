import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        
        for num in stones:
            heapq.heappush(heap, -num)

        while True:

            if len(heap) == 0:
                return 0

            if len(heap) == 1:
                return -heap[0]

            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y:
                continue

            if x > y:
                heapq.heappush(heap, -(x - y))
