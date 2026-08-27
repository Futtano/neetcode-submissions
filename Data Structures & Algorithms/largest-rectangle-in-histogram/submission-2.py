class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            if len(stack) == 0 or heights[i] > stack[-1][1]:
                stack.append((i, heights[i]))
                continue
            to_reinsert = []
            while len(stack) > 0 and heights[i] < stack[-1][1]:
                window_idx, window_height = stack[-1]
                area = (i - window_idx) * window_height
                max_area = max(max_area, area)
                to_reinsert.append((window_idx, heights[i]))
                stack.pop()
            stack.extend(to_reinsert)
            
        
        while(len(stack) > 0):
            window_idx, window_height = stack[-1]
            area = (len(heights) - window_idx) * window_height
            max_area = max(max_area, area)
            stack.pop()

        return max_area