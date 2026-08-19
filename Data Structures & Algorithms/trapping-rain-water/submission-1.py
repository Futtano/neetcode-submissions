class Solution:
    # Time: O(N)
    # Space: O(1)
    def trap(self, height: List[int]) -> int:
        # The formula for the amount of water that
        # can be trapped into position i  is min(max(height[:i]), max(height[i+1:])) - height[i]

        # We can solve this in O(1) space by using
        # two pointers and keeping track of the max
        # left and right height we've seen so far

        if not height:
            return 0

        l, r = 0, len(height)-1
        max_left, max_right = height[l], height[r]
        trapped = 0
    
        while(l < r):
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                trapped += max_left - height[l]
            else:
                r -=1
                max_right = max(max_right, height[r])
                trapped += max_right - height[r]

        return trapped


        