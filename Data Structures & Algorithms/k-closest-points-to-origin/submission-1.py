import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        def distance(x, y):
            d = (x)**2 + (y)**2
            d = math.sqrt(d)
            return d


        for p in points:

            dist = distance(p[0], p[1])

            heapq.heappush(heap, (dist, p))


        ans = []

        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans