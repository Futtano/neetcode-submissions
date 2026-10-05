class Solution:
    # Explicit stack DFS
    # Time: O(n^2)
    # Space: O(n^2)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        height = len(grid)
        width = len(grid[0])
        max_size = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 0:
                    continue

                stack = [(y, x)]
                grid[y][x] = 0
                size = 0

                while stack:
                    cy, cx = stack.pop()
                    size += 1

                    for dy, dx in directions:
                        ny, nx = cy + dy, cx + dx
                        if (
                            0 <= ny < height
                            and 0 <= nx < width
                            and grid[ny][nx] == 1
                        ):
                            grid[ny][nx] = 0
                            stack.append((ny, nx))

                max_size = max(max_size, size)

        return max_size