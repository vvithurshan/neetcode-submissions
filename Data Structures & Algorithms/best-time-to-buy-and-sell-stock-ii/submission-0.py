class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        TotalPro = 0

        for price in prices[1:]:
            if price < prev:
                prev = price
            else:
                profit = price - prev
                TotalPro += profit
                prev = price
        return TotalPro