class Solution:
    # Unbounded Knapsack with Bottom-Up DP
    # Let n = len(coins) and a = amount
    # Time complexity: O(n(a+1))
    # Space complexity: O(a+1)
    def coinChange(self, coins: List[int], amount: int) -> int:
        best = [float("inf") for _ in range(amount + 1)]
        best[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    best[a] = min(best[a], 1 + best[a-coin])

        return best[amount] if best[amount] != float("inf") else -1