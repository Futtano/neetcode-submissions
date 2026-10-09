class Solution:
    # 2D Dynamic Programming
    # Let m = sum(nums) and n = len(nums)
    # Time: O(n*m)
    # Space: O(n*m)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache= {}
        def ways(pos: int, amount: int) -> int:
            # All the way to the end, return 1 only if we matched target
            if pos == len(nums):
                return int(amount == target)
            # Already explored, return cached result
            if (pos, amount) in cache:
                return cache[(pos, amount)]

            # Explore both adding and subtracting the current element
            add = ways(pos+1, amount + nums[pos])
            sub = ways(pos+1, amount - nums[pos])

            # Cache and return the sum of the combinations returned by the two branches
            cache[(pos, amount)] = add + sub

            return cache[(pos, amount)]
            
        return ways(0, 0)