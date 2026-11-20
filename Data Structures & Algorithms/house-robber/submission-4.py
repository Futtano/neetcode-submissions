class Solution:
	def rob(self, nums: List[int]) -> int:
		cache = [None] * len(nums)

		def dp(i: int) -> int:
			if i >= len(nums):
				return 0

			if cache[i] is not None:
				return cache[i]

			cache[i] = max(
				nums[i] + dp(i+2),
				dp(i+1)
			)

			return cache[i]

		return dp(0)
