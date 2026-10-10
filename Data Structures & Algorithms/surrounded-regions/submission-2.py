class Solution:
    # DFS solution
    # Time: O(m*n)
    # Space: O(m*n)
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        queue = deque()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def enqueue(r, c):
            if board[r][c] == "O":
                board[r][c] = "T"
                queue.append((r, c))

        for col in range(cols):
            enqueue(0, col)
            enqueue(rows - 1, col)

        for row in range(rows):
            enqueue(row, 0)
            enqueue(row, cols - 1)

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    enqueue(nr, nc)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"