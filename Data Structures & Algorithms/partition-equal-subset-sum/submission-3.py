class Solution:
    # Knapsack 0/1 using top-down dynamic programming
    # Let n = len(nums) and T = sum(nums) // 2
    # Time complexity: O(nT)
    # Space complexity: O(nT)
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        cache = [[None for _ in range(target+1)] for _ in range(len(nums))]

        def dp(i: int, remaining: int) -> bool:
            if remaining == 0:
              return True
            if remaining < 0 or i == len(nums):
                return False

            if cache[i][remaining] is not None:
                return cache[i][remaining]

            cache[i][remaining] = (
                dp(i+1, remaining - nums[i]) or
                dp(i+1, remaining)	
            )

            return cache[i][remaining]

        return dp(0, target)