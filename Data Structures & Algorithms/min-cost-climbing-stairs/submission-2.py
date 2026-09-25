class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * 2

        for i in range(2, n + 1):
            dp[i % 2] = min(
                dp[(i - 1) % 2] + cost[i - 1],
                dp[(i - 2) % 2] + cost[i - 2]
            )

        return dp[n%2]