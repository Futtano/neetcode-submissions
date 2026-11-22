class Solution:
	# Unbounded Knapsack with Top-Down DP
	# Let n = len(coins) and a = amount
	# Time complexity: O(na)
	# Space complexity: O(na)
	def coinChange(self, coins: List[int], amount: int) -> int:
		cache = [
            [None for _ in range(amount+1)]
            for _ in range(len(coins))
        ]

		def dfs(i: int, remaining: int) -> int:
			if remaining == 0:
				return 0
			if remaining < 0 or i == len(coins):
				return float("inf")
			
			if cache[i][remaining] is not None:
				return cache[i][remaining]

			skip = dfs(i + 1, remaining)
			take = 1 + dfs(i, remaining - coins[i])
			cache[i][remaining] = min(skip, take)
			
			return cache[i][remaining]

		minCoins = dfs(0, amount)
		return minCoins if minCoins != float("inf") else -1
				