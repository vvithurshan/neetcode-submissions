from heapq import heappop, heappush, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        heapify(h)

        for i in stones:
            heappush(h, -i)

        while len(h) > 1:
            a = heappop(h)
            b = heappop(h)

            r = abs(abs(a) - abs(b))

            if r:
                heappush(h, -r)
        if h:
            return -heappop(h)
        return 0
