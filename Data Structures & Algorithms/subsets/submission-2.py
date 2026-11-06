class Solution:
    # Subsets using take-or-skip backtracking
    # Let n = len(nums).
    # Time complexity: O(n * 2^n), including the cost of copying subsets
    # Space complexity: O(n) auxiliary, excluding the output
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(i: int, path: List[int]) -> None:
            # path holds the elements chosen from nums[:i].
            if i == len(nums):
                # Save a snapshot because later branches modify the shared list.
                result.append(path.copy())
                return

            # Take nums[i] and decide what to do with the remaining elements.
            path.append(nums[i])
            dfs(i + 1, path)

            # Undo the choice so the skip branch starts with the original path.
            path.pop()
            dfs(i + 1, path)

        dfs(0, [])
        return result
        