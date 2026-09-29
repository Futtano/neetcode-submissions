class Solution:
    # Backtracking and checking previously placed queens
    # Time: O(n * n! + S * n^2)
    # Space: O(n^2 + S * n^2), including the output
    #        O(n^2), excluding the output

    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []  # Coordinates of the placed queens

        def backtrack():
            # One queen has been placed in every row.
            if len(state) == n:
                board = [['.'] * n for _ in range(n)]

                for row, col in state:
                    board[row][col] = 'Q'

                solutions.append([''.join(row) for row in board])
                return

            # The number of queens determines the next row.
            row = len(state)

            for col in range(n):
                valid = True

                # Check this position against every placed queen.
                for previous_row, previous_col in state:
                    same_column = col == previous_col
                    same_diagonal = (
                        abs(row - previous_row)
                        == abs(col - previous_col)
                    )

                    if same_column or same_diagonal:
                        valid = False
                        break

                if not valid:
                    continue

                # Choose this position.
                state.append((row, col))

                # Explore placements in the following rows.
                backtrack()

                # Undo the choice.
                state.pop()

        backtrack()
        return solutions