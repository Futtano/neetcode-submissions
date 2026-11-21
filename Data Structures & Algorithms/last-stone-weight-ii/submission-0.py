class Solution:
    # Knapsack 0/1 with top-down dynamic programming
    # Let n = len(stones) and T = sum(stones) // 2
    # Time complexity: O(nT)
    # Space complexity: O(nT)
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        
        cache = [[None for _ in range(target+1)] for _ in range(len(stones))]

        def dp(i: int, capacity: int) -> int:
            if i == len(stones) or capacity == 0:
                return 0

            if cache[i][capacity] is not None:
                return cache[i][capacity]

            cache[i][capacity] = max(
                stones[i] + dp(i + 1, capacity - stones[i]) if stones[i] <= capacity else 0,
                dp(i + 1, capacity),
            )

            return cache[i][capacity]

        return total - 2 * dp(0, target)