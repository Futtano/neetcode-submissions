class Solution:
    # Search for a word using DFS with path-specific cell marking
    # Let R = len(board), C = len(board[0]), and L = len(word).
    # Time complexity: O(R * C * 3^L)
    # Space complexity: O(min(L, R * C)) auxiliary recursion stack
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            # All characters were matched by previous calls.
            if i == len(word):
                return True

            # Reject out-of-bounds cells, mismatches and used cells.
            # The "#" marker cannot match a letter in the word.
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or board[r][c] != word[i]
            ):
                return False

            # Reserve this cell for the current path.
            original = board[r][c]
            board[r][c] = "#"

            # Any successful direction completes a valid continuation.
            found = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            # Restore even after success so the board remains unchanged.
            board[r][c] = original
            return found

        # Only cells matching the first character can start the word.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False