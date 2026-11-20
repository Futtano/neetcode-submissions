class Solution:
    # Bottom-up DP
    # Time complexity: O(n)
    # Space complexity: O(1)
	def rob(self, nums: List[int]) -> int:
		if len(nums) < 2:
			return nums[0]

		dp = [max(nums[-2], nums[-1]), nums[-1]]

		for i in range(len(nums) - 3, -1, -1):
			new = max(
				nums[i] + dp[1],
				dp[0]
			)
			dp[0], dp[1] = new, dp[0]

		return max(dp[0], dp[1])


