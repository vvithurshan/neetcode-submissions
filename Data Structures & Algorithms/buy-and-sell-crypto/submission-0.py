class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        curr = prices[0]
        for price in prices[1:]:
            if price - curr > 0:
                maxP = max(maxP, price - curr)
            else:
                curr = price
        return maxP