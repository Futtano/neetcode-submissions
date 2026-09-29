class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a = nums[0]
        b = nums[1]

        for i in range (2, len(nums)):
            if i % 2 == 0:
                interval_max = max(a, b)
                a += nums[i]
            else:
                b = nums[i] + interval_max

        return max(a,b)


