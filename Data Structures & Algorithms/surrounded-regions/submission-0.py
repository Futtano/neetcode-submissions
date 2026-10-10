class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        edge_zeros = set()
        processed = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for col in range(cols):
            if board[0][col] == "O":
                edge_zeros.add((0, col))
        
        for col in range(cols):
            if board[rows-1][col] == "O":
                edge_zeros.add((rows-1, col))
        
        for row in range(rows):
            if board[row][0] == "O":
                edge_zeros.add((row, 0))
        
        for row in range(rows):
            if board[row][cols-1] == "O":
                edge_zeros.add((row, cols-1))

        def bfs(r, c):
            if (r,c) in processed:
                return

            processed.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (
                    0 <= nr < rows and 
                    0 <= nc < cols and
                    board[nr][nc] == 'O'
                ):
                    bfs(nr, nc)

        for r, c in edge_zeros:
            bfs(r, c)

        for row in range(rows):
            for col in range(cols):
                if (
                    (row, col) not in processed and
                    (row, col) not in edge_zeros
                ):
                    board[row][col] = 'X'
                    


