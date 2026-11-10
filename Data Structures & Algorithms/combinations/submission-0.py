class Solution:
    # Generate fixed-size combinations with loop-based backtracking
    # Let C = binomial(n, k), the number of returned combinations.
    # Time complexity: O(k * C)
    # Space complexity: O(k) auxiliary, excluding O(k * C) output
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []

        def dfs(start: int) -> None:
            # Save a snapshot once we have chosen exactly k numbers.
            if len(path) == k:
                res.append(path.copy())
                return

            needed = k - len(path)

            # Choosing value leaves n - value larger numbers.
            # Require n - value >= needed - 1, so value <= n - needed + 1.
            # Add one more because range excludes its upper endpoint.
            for value in range(start, n - needed + 2):
                path.append(value)

                # Choose only larger numbers to avoid reuse and duplicates.
                dfs(value + 1)

                # Restore the path before trying the next possible value.
                path.pop()

        dfs(1)
        return res