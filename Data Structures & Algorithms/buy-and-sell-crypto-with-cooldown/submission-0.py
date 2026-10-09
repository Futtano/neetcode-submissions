class Solution:
    # 2D Dynamic programming
    # Time: O(n)
    # Space: O(n)
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def profit(buyed: bool, day: int) -> int:
            if day >= len(prices):
                return 0
            if (buyed, day) in cache:
                return cache[(buyed, day)]
            
            # Do nothing today
            skip = profit(buyed, day + 1)

            # Buy today and recurse to tomorrow
            if not buyed:
                action = \
                    -prices[day] + profit(True, day+1)
            # Sell today and recurse two days from today
            else:
                action = \
                    prices[day] + profit(False, day+2) 
            
            cache[(buyed, day)] = max(
                skip, action
            ) 

            return cache[(buyed, day)]
        
        return profit(False, 0)