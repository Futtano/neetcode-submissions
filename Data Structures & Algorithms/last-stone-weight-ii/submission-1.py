class Solution:
    # Last Stone Weight II using top-down 0/1 knapsack
    # Let n = len(stones) and T = sum(stones) // 2.
    # Time complexity: O(n(T + 1))
    # Space complexity: O(n(T + 1)) for the cache, plus O(n) for recursion
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total = sum(stones)
        target = total // 2
        n = len(stones)
        cache = [[None] * (target + 1) for _ in range(n)]

        def dp(i: int, capacity: int) -> int:
            # Largest weight we can choose from stones[i:] within capacity.
            if i == n or capacity == 0:
                return 0

            if cache[i][capacity] is None:
                best = dp(i + 1, capacity)  # Skip the current stone.

                weight = stones[i]
                if weight <= capacity:
                    # Take this stone and fill the remaining capacity.
                    best = max(best, weight + dp(i + 1, capacity - weight))

                cache[i][capacity] = best

            return cache[i][capacity]

        # The two groups weigh lighter and total - lighter.
        lighter = dp(0, target)
        return total - 2 * lighter