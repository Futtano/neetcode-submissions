class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = total = 0
        
        for i, el in enumerate(nums):
            expected += i
            total += el

        expected += len(nums)

        return expected - total