class Solution:
    # Find unique combinations using take-or-skip backtracking
    # Let n = len(nums), a = min(nums), and D = target // a.
    # Let R be the number of returned combinations.
    # Time complexity: O(2^(n + D) + R * D), a loose upper bound
    # Space complexity: O(n + D) auxiliary, excluding the output
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []

        def dfs(i: int, remaining: int) -> None:
            # A complete combination needs no more values.
            if remaining == 0:
                res.append(path.copy())
                return

            # Stop if we exceed the target or exhaust all candidates.
            if remaining < 0 or i == len(nums):
                return

            # Take nums[i]. Stay at i so this value can be reused.
            path.append(nums[i])
            dfs(i, remaining - nums[i])

            # Undo the take before exploring combinations that skip this value.
            path.pop()
            dfs(i + 1, remaining)

        dfs(0, target)
        return res