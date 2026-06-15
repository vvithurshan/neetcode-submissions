from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], x: int) -> int:
        @lru_cache(None)
        def dp(amt):
            if amt < 0:
                return float('inf')
            if amt == 0:
                return 0

            ans = float('inf')
            for coint in coins:
                result = dp(amt - coint)
                if result != float('inf'):
                    ans = min(ans, result + 1)
            return ans

        result = dp(x)
        return -1 if result == float('inf') else result