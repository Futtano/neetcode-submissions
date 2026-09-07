class Solution:
    # Dynamic Programming
    # Time: O(n)
    # Space O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Build two arrays to keep track of the max to the left and to 
        # the right of each position i (included) for each block of k
        # items
        left_max = [0] * len(nums)
        right_max = [0] * len(nums)

        res = [0] * (len(nums) - k + 1)

        l = 0 
        r = min(k, len(nums))

        # Fill the left_max array and right_max arrays
        while(l < len(nums)):
            curr_max = nums[l]
            for i in range(l, r):
                curr_max = max(curr_max, nums[i])
                left_max[i] = curr_max

            curr_max = nums [r-1]
            for i in reversed(range(l, r)):
                curr_max = max(curr_max, nums[i])
                right_max[i] = curr_max

            l += k
            r = min(l + k, len(nums))

        # The max in the i-th window is the max
        # between the right_max at pos i and left_max
        # at position j (the last position of the current
        # window)
        for i in range(len(nums) - k + 1):
            j = i + k -1
            res[i] = max(right_max[i], left_max[j])

        return res