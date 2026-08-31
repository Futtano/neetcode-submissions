class Solution:
    # Time:     O(n)
    # Space:    O(1)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1 # l = buy day, r = sell day

        while r < len(prices):
            if prices[r] > prices[l]: # if we can make a profit
                max_profit = max(max_profit, prices[r] - prices[l]) # check if it is the best profit
            else:
                # we found a lower or equal price than the current one, so we can 
                # switch the buy day to it
                l = r
            r += 1 # advance through sell days
        
        return max_profit