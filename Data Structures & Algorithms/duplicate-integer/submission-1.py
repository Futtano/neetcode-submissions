class Solution:
    # Time: O(nlogn) sorting
    # Space: O(1) 
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # in-place sort

        # Now if there is any duplicate,
        # they are adjacent
        for i in range(1, len(nums)): 
            if nums[i-1] == nums[i]:
                return True

        return False