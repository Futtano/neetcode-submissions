class Solution:
    # Greedy
    # Time: O(n)
    # Space: O(1)
    def canJump(self, nums: List[int]) -> bool:
        # start at index 0 with nums[0] available steps
        # to proceed
        availableSteps = nums[0]
        pos = 0
        end = len(nums) - 1
        while pos < end and (availableSteps or nums[pos]):
            # Take the max between how many steps we have left
            # from previous advances and the steps available
            # at the current location
            availableSteps = max(availableSteps, nums[pos])
            # Advance one step at a time
            availableSteps -= 1
            pos += 1

        # Return true only if we arrived at the last index
        return pos == end
        
