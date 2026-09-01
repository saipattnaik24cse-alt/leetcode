class Solution:
    def maxProfit(self, prices):
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                profit = prices[i] - minPrice
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
        


        
        