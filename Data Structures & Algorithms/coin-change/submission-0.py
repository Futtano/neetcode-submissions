class Solution:
    # Time: O(A*C) = O(A) where A is the amount and C is the number of coins
    # Space: O(A)
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [None] * (amount+1)

        def minCoins(rest: int) -> int:
            if rest == 0:
                return 0
            if cache[rest] is not None:
                return cache[rest]

            best = float('inf')
            for coin in coins:
                if coin <= rest:
                    nCoins = minCoins(rest - coin)
                    if nCoins != -1:
                        best = min(best, 1 + nCoins)
            
            cache[rest] = -1 if best == float('inf') else best

            return cache[rest]
                
        return minCoins(amount)

