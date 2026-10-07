class Solution:
    # Kadane's Algorithm
    # Time: O(n)
    # Space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]

        for el in nums[1:]:
            cur_sum = max(el, cur_sum + el)
            max_sum = max(max_sum, cur_sum)

        return max_sum