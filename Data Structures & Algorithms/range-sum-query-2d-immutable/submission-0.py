class NumMatrix:
    # 2D prefix sums
    # Time O(r*c)
    # Space O(r*c)
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])

        # prefix[r][c] sums the first r rows and first c columns.
        # The extra zero row and column handle boundary cases.
        self.prefix = [
            [0] * (cols + 1)
            for _ in range(rows + 1)
        ]
        prefix = self.prefix

        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c + 1] = (
                    matrix[r][c]
                    + prefix[r][c + 1]      # Above
                    + prefix[r + 1][c]      # Left
                    - prefix[r][c]          # Remove duplicated overlap
                )

    # Query time: O(1)
    def sumRegion(
        self,
        row1: int,
        col1: int,
        row2: int,
        col2: int,
    ) -> int:
        prefix = self.prefix

        # Bottom/right indices are inclusive, so add 1.
        bottom, right = row2 + 1, col2 + 1

        return (
            prefix[bottom][right]
            - prefix[row1][right]   # Remove rows above the region
            - prefix[bottom][col1]  # Remove columns left of the region
            + prefix[row1][col1]    # Restore overlap removed twice
        )