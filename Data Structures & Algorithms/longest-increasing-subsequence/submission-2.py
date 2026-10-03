class Solution:
    # Recursive dynamic programming
    # Time: O(n^2)
    # Space: O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def endingAt(i: int) -> int:
            if i in cache:
                return cache[i]

            best = 1  # nums[i] alone

            for j in range(i):
                if nums[j] < nums[i]:
                    best = max(best, endingAt(j) + 1)

            cache[i] = best
            return best

        return max(endingAt(i) for i in range(len(nums)))