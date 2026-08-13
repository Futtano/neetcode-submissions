class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We use a sort + two pointers approach
        srtd_nums = sorted(nums) 
        # the original indexes sorted as the srtd_nums list
        srtd_idx = sorted(range(0, len(nums)), key=lambda k: nums[k])

        # We start with the indexes at both ends of the sorted array
        l = 0
        r = len(nums) - 1

        while(l < r): # while we do not cross the two pointers
            if (nums[l] + nums[r]) < target:
                l += 1 # increase l to have a bigger sum
            elif (nums[l] + nums[r]) > target:
                r -= 1 # decreas r to have a lower sum
            else: # we found the sum return, the original positions of the pointers
                return [srtd_idx[l], srtd_idx[r]]

        # For consistency, this will never be reached as the solution
        # always exist as the problem states
        return [srtd_idx[l], srtd_idx[r]]
        