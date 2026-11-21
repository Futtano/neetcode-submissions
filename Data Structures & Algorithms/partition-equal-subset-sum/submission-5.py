class Solution:
    # Partition Equal Subset Sum using bottom-up 0/1 knapsack
    # Let n = len(nums) and T = sum(nums) // 2.
    # Time complexity: O(nT)
    # Space complexity: O(T)
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        # A subset summing to target leaves the same sum for the other group.
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True  # The empty subset makes sum zero.

        for num in nums:
            # Scan downward so dp[s - num] still describes the previous pass.
            # This lets us take the current occurrence of num at most once.
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]  # Skip num or take it.

            if dp[target]:
                return True

        return dp[target]