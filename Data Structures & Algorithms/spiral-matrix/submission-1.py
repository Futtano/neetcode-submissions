class Solution:
    # m = number of rows, n = number of columns.
    # Time: O(m * n). Auxiliary space: O(1), excluding the output.
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        startRow, startCol = 0, 0
        endRow, endCol = m - 1, n - 1
        res = []

        while startRow <= endRow and startCol <= endCol:
            if startRow == endRow:
                for j in range(startCol, endCol + 1):
                    res.append(matrix[startRow][j])
                break

            if startCol == endCol:
                for i in range(startRow, endRow + 1):
                    res.append(matrix[i][startCol])
                break

            # Each side excludes the corner where the next side begins.
            for j in range(startCol, endCol):
                res.append(matrix[startRow][j])
            for i in range(startRow, endRow):
                res.append(matrix[i][endCol])
            for j in range(endCol, startCol, -1):
                res.append(matrix[endRow][j])
            for i in range(endRow, startRow, -1):
                res.append(matrix[i][startCol])

            startRow += 1
            endRow -= 1
            startCol += 1
            endCol -= 1

        return res