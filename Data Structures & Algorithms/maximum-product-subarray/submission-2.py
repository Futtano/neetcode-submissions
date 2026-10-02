class Solution:
    # Optimal DP solution
    # Time: O(n)
    # Space: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        currentMax = nums[0]
        currentMin = nums[0]
        ans = nums[0]

        for x in nums[1:]:
            a = x
            b = x * currentMax
            c = x * currentMin

            currentMax = max(a, b, c)
            currentMin = min(a, b, c)
            ans = max(ans, currentMax)

        return ans