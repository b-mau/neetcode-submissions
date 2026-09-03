class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit = price - min_price
            max_profit = max(profit, max_profit)
            min_price = min(price, min_price)
        
        return max_profit