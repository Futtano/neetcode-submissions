class Solution:
    # Backtracking with sets for conflict checking
    # Time: O(n! + S * n^2)
    # Space: O(n^2 + S * n^2), including the output
    #        O(n^2), excluding the output

    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        columns = set()
        descending_diagonals = set()  # Identified by row - col
        ascending_diagonals = set()   # Identified by row + col

        board = [['.'] * n for _ in range(n)]

        def backtrack(row):
            # One queen has been placed in every row.
            if row == n:
                solutions.append([''.join(line) for line in board])
                return

            for col in range(n):
                descending = row - col
                ascending = row + col

                # All three conflict checks are O(1).
                if (
                    col in columns
                    or descending in descending_diagonals
                    or ascending in ascending_diagonals
                ):
                    continue

                # Place the queen and record the occupied lines.
                board[row][col] = 'Q'
                columns.add(col)
                descending_diagonals.add(descending)
                ascending_diagonals.add(ascending)

                backtrack(row + 1)

                # Remove the queen and restore the previous state.
                board[row][col] = '.'
                columns.remove(col)
                descending_diagonals.remove(descending)
                ascending_diagonals.remove(ascending)

        backtrack(0)
        return solutions