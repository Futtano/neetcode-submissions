class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left_max = [0] * len(nums)
        right_max = [0] * len(nums)
        res = [0] * (len(nums) - k + 1)

        l = 0 
        r = min(k, len(nums))

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

        for i in range(len(nums) - k + 1):
            j = i + k -1
            res[i] = max(right_max[i], left_max[j])

        return res