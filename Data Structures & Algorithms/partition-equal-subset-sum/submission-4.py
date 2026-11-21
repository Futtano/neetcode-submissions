class Solution:
    # Partition Equal Subset Sum using top-down 0/1 knapsack
    # Let n = len(nums) and T = sum(nums) // 2.
    # Time complexity: O(nT)
    # Space complexity: O(nT) for the cache and O(n) for the recursion stack
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        # A subset summing to target leaves exactly target for the other group.
        target = total // 2
        n = len(nums)
        cache = [[None] * (target + 1) for _ in range(n)]

        def dp(i: int, remaining: int) -> bool:
            # Can nums[i:] supply exactly the remaining sum?
            if remaining == 0:
                return True
            if i == n or remaining < 0:
                return False

            # Both True and False are cached answers. None means uncomputed.
            if cache[i][remaining] is None:
                # Advance past this item in both branches so it is used at most once.
                cache[i][remaining] = (
                    dp(i + 1, remaining - nums[i])
                    or dp(i + 1, remaining)
                )

            return cache[i][remaining]

        return dp(0, target)