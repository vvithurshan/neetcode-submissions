class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r

        while l <= r:

            mid = l + (r - l)//2

            total = 0

            for p in piles:
                t = p // mid if p % mid == 0 else (p // mid) + 1
                total += t

            if total <= h:
                res = min(res, mid)
                r = mid - 1
                
            else: # if total > h
                l = mid + 1

        return res