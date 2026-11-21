class Solution:
    # Last Stone Weight II using bottom-up 0/1 knapsack
    # Let n = len(stones) and T = sum(stones) // 2.
    # Time complexity: O(n * (T + 1))
    # Space complexity: O(T + 1) for one row of DP states
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total = sum(stones)
        target = total // 2

        # With no stones, the largest weight that fits any capacity is zero.
        best = [0] * (target + 1)

        for weight in stones:
            # Scan downward so best[capacity - weight] still describes
            # a subset formed before the current stone was available.
            for capacity in range(target, weight - 1, -1):
                skip = best[capacity]
                take = weight + best[capacity - weight]
                best[capacity] = max(skip, take)

        # The groups weigh lighter and total - lighter.
        # Maximizing lighter minimizes the difference between them.
        lighter = best[target]
        return total - 2 * lighter