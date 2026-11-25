class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        best_price = -1
        for i in range(len(prices)):
            if i <= 0: # skip first item
                continue
            # If the best price value is lower than buy day before it and NOT 0 (so it has an actual val)
            if best_price >= 0 and best_price < prices[i - 1]:  
                profit = prices[i] - best_price
                if profit > maximum:
                    maximum = profit
            else: # Otherwise reset
                best_price = prices[i - 1]
                profit = prices[i] - best_price 
                if profit > maximum:
                    maximum = profit
        return maximum