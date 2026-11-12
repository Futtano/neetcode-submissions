class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        time = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        moves = ((0,1), (0, -1), (1,0), (-1,0))

        while queue and fresh:
            n = len(queue)
            for _ in range(n):
                r, c = queue.popleft()
                for mr, mc in moves:
                    nr, nc = r+mr, c+mc
                    if (	
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))
            time += 1

        return time if fresh == 0 else -1
