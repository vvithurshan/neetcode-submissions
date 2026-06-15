from heapq import heappop, heappush, heapify

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        heapify(h)

        for coor in points:
            d = math.sqrt(coor[0]**2 + coor[1]**2)
            heappush(h, [d, coor])

        ans = []
        for _ in range(k):
            ans.append(heappop(h)[1])
        return ans