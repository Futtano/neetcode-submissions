class Solution:
    # Time: O(n)
    # Space: O(n)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robHelper(start, end):
            prev1, prev2 = 0, 0
            for i in range(start, end):
                prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
            return prev1

        return max(
            robHelper(0, len(nums) - 1),
            robHelper(1, len(nums))
        )