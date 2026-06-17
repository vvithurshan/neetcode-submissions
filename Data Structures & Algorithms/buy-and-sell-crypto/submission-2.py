class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        maxProf = 0

        for price in prices:

            curProf = price - minPrice
            if curProf < 0:
                minPrice = price

            else:
                maxProf = max(maxProf, curProf)

        return maxProf

