class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache= {}
        def ways(pos: int, amount: int) -> int:
            if amount == target and pos == len(nums):
                return 1
            if pos == len(nums):
                return 0
            if (pos, amount) in cache:
                return cache[(pos, amount)]

            add = ways(pos+1, amount + nums[pos])
            sub = ways(pos+1, amount - nums[pos])

            cache[(pos, amount)] = \
                add + sub

            return add + sub
            
        return ways(0, 0)