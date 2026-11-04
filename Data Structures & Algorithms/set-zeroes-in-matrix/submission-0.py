class Solution:
    # Use the first row and column as in-place zero markers
    # Let r = len(matrix), c = len(matrix[0]).
    # Time complexity: O(r * c)
    # Space complexity: O(1)
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        # Preserve their original zero status before writing markers.
        zero_first_row = any(matrix[0][j] == 0 for j in range(cols))
        zero_first_col = any(matrix[i][0] == 0 for i in range(rows))

        # Mark affected rows and columns using only interior original zeros.
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Apply markers without overwriting the marker row or column.
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Clear the marker row and column only after all markers are consumed.
        if zero_first_row:
            for j in range(cols):
                matrix[0][j] = 0

        if zero_first_col:
            for i in range(rows):
                matrix[i][0] = 0