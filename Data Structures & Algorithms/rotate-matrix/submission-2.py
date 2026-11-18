class Solution:
    # n is the number of rows and columns.
    # Time: O(n²). Auxiliary space: O(1).
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # Transpose in place. Visit each off-diagonal pair once.
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse every row in place.
        for row in matrix:
            row.reverse()