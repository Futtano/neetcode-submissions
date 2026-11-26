class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums) + 1
        self.prSum = [0] * n

        for i in range(1, n):
            self.prSum[i] = self.prSum[i-1] + nums[i-1] 

    def sumRange(self, left: int, right: int) -> int:
        return self.prSum[right+1] - self.prSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)