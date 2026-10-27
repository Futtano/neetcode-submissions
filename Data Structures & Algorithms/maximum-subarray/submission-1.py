class Solution:
    # Prefix Sum
    # Time: O(n)
    # Space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        run = minPref = 0
        res = nums[0]
        for el in nums:
            run += el
            res = max(res, run - minPref)
            minPref = min(minPref, run)

        return res
