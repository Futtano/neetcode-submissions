class Solution:
    # 2D Dynamic Programming
    # Let len(coins) = n and amount = m
    # Time: O(m*n)
    # Space: O(m*n)
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def combinations(pos:int, remaining: int) -> int:
            if remaining == 0:
                return 1
            if pos >= len(coins):
                return 0
            if (pos, remaining) in cache:
                return cache[(pos, remaining)]
            

            # skip current coin
            skip = combinations(pos+1, remaining)
            
            rest = remaining - coins[pos]
            take = 0
            # use the current coin if we can
            if rest >= 0:
                take = combinations(pos, rest)

            cache[(pos, remaining)] = skip + take

            return cache[(pos, remaining)]

        return combinations(0, amount)
             