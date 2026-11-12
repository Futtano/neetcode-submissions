class Solution:
    # Simulate rotting with multi-source BFS.
    # Let R and C be the number of rows and columns.
    # Time complexity: O(R * C)
    # Space complexity: O(R * C) auxiliary for the queue
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        minutes = 0
        queue = deque()

        # All initially rotten oranges start spreading at minute zero.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while queue and fresh > 0:
            # Process only the oranges that can spread this minute.
            level_size = len(queue)
            for _ in range(level_size):
                r, c = queue.popleft()

                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        # Mark before enqueueing so each orange is counted once.
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            minutes += 1

        return minutes if fresh == 0 else -1