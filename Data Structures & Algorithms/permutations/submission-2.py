class Solution:
    # Generate permutations by choosing each unused value
    # Let n = len(nums), whose values are distinct.
    # Time complexity: O(n * n!), assuming average O(1) set operations
    # Space complexity: O(n) auxiliary, excluding O(n * n!) output
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def backtrack(path: list[int]) -> None:
            # Every input value has been chosen exactly once.
            if len(path) == len(nums):
                # Save a snapshot before backtracking changes the shared path.
                res.append(path.copy())
                return

            for value in nums:
                if value not in used:
                    # Choose this value for the next position.
                    used.add(value)
                    path.append(value)

                    backtrack(path)

                    # Restore both structures before trying another choice.
                    path.pop()
                    used.remove(value)

        backtrack([])
        return res
    