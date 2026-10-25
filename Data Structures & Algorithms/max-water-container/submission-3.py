class Solution:
    # Two pointers
    # Time = O(n)
    # Space = O(1)
    def maxArea(self, heights: List[int]) -> int:
        # Invariant is that if heights[l] < heights[r],
        # Moving r inward cannot beat the current area, 
        # as the width of the container shrinks and
        # the height is capped by heights[l]
        # If the heigths[l] > heigths[r], we do the opposite so move
        # r. If both are equal, we can move either of the two.

        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res 
