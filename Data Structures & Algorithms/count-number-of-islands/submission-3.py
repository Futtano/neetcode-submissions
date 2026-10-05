class Solution:
    # Explicit Stack DFS
    # Time: O(n^2)
    # Space: O(n^2)
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        height, width = len(grid), len(grid[0])
        n_islands = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for y in range(height):
            for x in range(width):
                if grid[y][x] != "1":
                    continue

                n_islands += 1
                grid[y][x] = "0"
                stack = [(y, x)]

                while stack:
                    cy, cx = stack.pop()

                    for dy, dx in directions:
                        ny, nx = cy + dy, cx + dx

                        if (
                            0 <= ny < height
                            and 0 <= nx < width
                            and grid[ny][nx] == "1"
                        ):
                            grid[ny][nx] = "0"
                            stack.append((ny, nx))

        return n_islands