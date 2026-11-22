class Solution:
	# Unbounded Knapsak, Bottom-Up DP
	# Let n = len(coins) and a = amount
	# Time complexity: O(n(a+1))
	# Space complexity: O(a+1)
	def change(self, amount: int, coins: List[int]) -> int:
		dp = [0] * (amount + 1)
		dp[0] = 1

		for coin in coins:
			for s in range(coin, amount + 1):
				dp[s] += dp[s-coin]

		return dp[amount]