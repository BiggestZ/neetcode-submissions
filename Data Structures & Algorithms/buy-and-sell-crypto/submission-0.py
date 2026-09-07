class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l: Buy, r: Sell
        l, r = 0,1
        maxP = 0
        while r < (len(prices)):
            if prices[l] < prices[r]: # While L < R, check profit
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit) # Compare Profit
            else:
                l=r
            r+=1
        return maxP