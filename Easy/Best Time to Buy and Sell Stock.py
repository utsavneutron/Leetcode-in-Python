class Solution:
    def maxProfit(self, prices) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            if(minPrice > prices[i]):
                minPrice = prices[i]
            else:
                if(prices[i] - minPrice > maxProfit):
                    maxProfit = prices[i] - minPrice

        return maxProfit
