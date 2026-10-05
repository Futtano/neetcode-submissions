class Solution:
    # Recursive DFS
    # Time: O(n^2)
    # Space: O(n^2)
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        height, width = len(grid), len(grid[0])
        n_islands = 0

        def discover(y: int, x: int) -> None:
            if not (0 <= y < height and 0 <= x < width):
                return
            if grid[y][x] != "1":
                return

            grid[y][x] = "0"
            discover(y + 1, x)
            discover(y - 1, x)
            discover(y, x + 1)
            discover(y, x - 1)

        for y in range(height):
            for x in range(width):
                if grid[y][x] == "1":
                    n_islands += 1
                    discover(y, x)

        return n_islands