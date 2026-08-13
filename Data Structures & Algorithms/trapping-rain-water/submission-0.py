class Solution:
    def trap(self, height: List[int]) -> int:
        slow = 0
        fast = 1
        water = 0

        while(fast < len(height)):
            # Slide until we found concavity
            while(height[slow] <= height[fast]):
                slow +=1
                fast += 1

            # Increase fast until we either end the array
            # or we found a bar >= heights[slow]
            # Also keep track of bar heights to be subtracted
            # later
            bars = 0
            while(fast < len(height) and height[fast] < height[slow]):
                fast += 1
                bars += height[fast-1]
                

            if fast != len(height): # 
            # We found the pool boundaries
                area = (fast - slow - 1) * min(height[slow], height[fast])
                water += (area - bars)

            # Processed the pool now keep going forward
            slow = fast
            fast += 1

        return water