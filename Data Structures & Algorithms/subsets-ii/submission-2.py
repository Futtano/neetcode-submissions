class Solution:
    # Generate unique subsets by skipping duplicate values together
    # Let n = len(nums).
    # Time complexity: O(n log n + n * 2^n) = O(n * 2^n)
    # Space complexity: O(n) auxiliary, excluding the output
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sorting groups equal values so the skip branch can bypass them.
        nums.sort()
        path = []
        res = []

        def dfs(i: int) -> None:
            if i == len(nums):
                # Save a snapshot before later branches modify the path.
                res.append(path.copy())
                return

            # Take this occurrence. The next occurrence remains available.
            path.append(nums[i])
            dfs(i + 1)

            # Undo the take, then exclude all remaining copies of this value.
            path.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res