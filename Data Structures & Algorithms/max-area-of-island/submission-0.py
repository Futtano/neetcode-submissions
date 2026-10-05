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
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

        for y in range(height):
            for x in range(width):
                if grid[y][x] == 0:
                    continue

                grid[y][x] = 0
                stack = [(y, x)]
                size = 1

                while stack:
                    y_b, x_b = stack.pop()
                    for pos in directions:
                        y_t = y_b + pos[0]
                        x_t = x_b + pos[1]
                        if (
                            0 <= y_t < height and
                            0 <= x_t < width and
                            grid[y_t][x_t] == 1
                        ):
                            grid[y_t][x_t] = 0
                            size += 1
                            stack.append((y_t, x_t))
                
                max_size = max(max_size, size)

        return max_size

                    