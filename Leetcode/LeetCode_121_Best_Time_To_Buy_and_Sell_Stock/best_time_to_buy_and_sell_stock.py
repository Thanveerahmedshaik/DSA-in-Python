# Best time to buy and sell stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.  
 
from typing import List

class Solution:
    """
    This function calculates the maximum profit from a single buy-sell transaction.
    It iterates through the list of prices, keeping track of the minimum price seen so far 
    and the maximum profit that can be achieved.
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = float("inf")
        max_profit = 0

        for i in range(n):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit
    
    # The time complexity of this approach is O(n) as it traverses the array once.
    # The space complexity is O(1) as it uses a constant amount of space.
# Example usage:
# sol = Solution()
# print(sol.maxProfit([7,1,5,3,6,4]))
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.    

