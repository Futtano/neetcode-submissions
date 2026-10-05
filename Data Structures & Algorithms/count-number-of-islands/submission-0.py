class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        n_islands = 0

        def discover(y: int, x: int, found: bool) -> None:
            nonlocal n_islands
            if 0 <= x < width and 0 <= y < height:
                if grid[y][x] == '1':
                    if not found:
                        found = True
                        n_islands += 1
                    grid[y][x] = '0'
                    discover(y+1, x, found)
                    discover(y-1, x, found)
                    discover(y, x+1, found)
                    discover(y, x-1, found)

        for i in range(height):
            for j in range(width):
                discover(i, j, False)

        return n_islands

