class Solution:
    # House Robber with rolling suffix DP
    # Let n = len(nums).
    # Time complexity: O(n)
    # Space complexity: O(1) auxiliary
    def rob(self, nums: list[int]) -> int:
        # Start with dp(n) and dp(n + 1), both empty suffixes.
        next_one = next_two = 0

        for i in range(len(nums) - 1, -1, -1):
            # Before this iteration, the values hold dp(i + 1) and dp(i + 2).
            best_here = max(next_one, nums[i] + next_two)

            # Carry dp(i) and dp(i + 1) into the next iteration.
            next_one, next_two = best_here, next_one

        return next_one