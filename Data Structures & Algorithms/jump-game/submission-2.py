class Solution:
    def canJump(self, nums: List[int]) -> bool:
        availableSteps = nums[0]
        pos = 0
        end = len(nums) - 1
        while pos < end and (availableSteps or nums[pos]):
            availableSteps = max(availableSteps, nums[pos])
            availableSteps -= 1
            pos += 1

        return pos == end
        
