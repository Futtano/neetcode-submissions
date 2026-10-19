class Solution:
    # Interval DP
    # Time: O(n^3)
    # Space: O(n^2)
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}

        def dp(l: int, r: int) -> int:
            if (l, r) in cache:
                return cache[(l, r)]
            if r - l <= 1:
                return 0 

            best = 0


            for i in range(l + 1, r):
                coins = nums[l] * nums[i] * nums[r]
                left = dp(l, i)
                right = dp(i, r)
                best = max(
                    best,
                    coins + left + right
                )

            cache[(l, r)] = best
            return best  

        return dp(0, len(nums) - 1)