class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        ans = r

        while l <=r :
            mid = (l + r)//2

            minh = 0

            for p in piles:
                hrs = p // mid if p % mid == 0 else (p // mid ) + 1
                minh += hrs

            if minh <= h:
                ans = min(ans, mid)
                r = mid - 1

            else:
                l = mid + 1

        return ans
