class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxh = max(piles)
        minh = maxh
        l = 1
        r = maxh
        while l <= r:
            mid = (l+r+1)//2
            currh = 0
            for pile in piles:
                currh += math.ceil(pile/mid)
            if currh <= h:
                # print(i, currh)
                minh = mid
                r = mid - 1
            else:
                l = mid + 1
        return minh