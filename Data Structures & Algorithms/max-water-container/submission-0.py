class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_amount = 0
        while(l < r):
            cur_amount = (r - l) * min(heights[l], heights[r])
            max_amount = max(max_amount, cur_amount)
            if heights[l] < heights[r]: # find a bigger heights[l]
                l += 1
                while(l < r and heights[l] < heights[l-1]):
                    l += 1
            else: # find a bigger heights[r]
                r -= 1
                while(l < r and heights[r] < heights[l+1]):
                    r -= 1
        
        return max_amount

            