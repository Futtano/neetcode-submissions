class Solution:
    # Kadane's algorithm for the maximum nonempty subarray sum
    # Let n = len(nums).
    # Time complexity: O(n)
    # Space complexity: O(1) auxiliary
    def maxSubArray(self, nums: list[int]) -> int:
        ending_here = best = nums[0]

        for i in range(1, len(nums)):
            value = nums[i]

            # Extend the best subarray ending at i - 1, or start at i.
            ending_here = max(ending_here + value, value)

            # Track the best sum across all endpoints seen so far.
            best = max(best, ending_here)

        return best