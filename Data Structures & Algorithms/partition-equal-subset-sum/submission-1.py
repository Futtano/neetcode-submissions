class Solution:
    # Time = O(n * t) where t is half the sum of the array
    # Space = O(n * t)
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        cache = {}

        def matchSum(index: int, cumSum: int) -> bool:
            if cumSum == target:
                return True

            if index == len(nums) or cumSum > target:
                return False

            state = (index, cumSum)
            if state in cache:
                return cache[state]

            cache[state] = (
                matchSum(index + 1, cumSum + nums[index])
                or matchSum(index + 1, cumSum)
            )
            return cache[state]

        return matchSum(0, 0)