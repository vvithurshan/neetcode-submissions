class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProf = 0
        minPrice = prices[0]

        for num in prices[1:]:
            if num < minPrice:
                minPrice = num

            else:
                maxProf = max(maxProf, (num - minPrice))

        return maxProf