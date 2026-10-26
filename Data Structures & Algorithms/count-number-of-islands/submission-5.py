class Solution:
    # Iterative DFS with an explicit stack
    # Time O(r*c)
    # Space O(r*c) 
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # Possible movements from a cell
        directions = ((-1, 0), (1, 0), (0 ,-1), (0, 1))
        res = 0

        stack = []

        for r in range(rows):
            for c in range(cols):
                # Found an islands, update result
                # and consume it
                if grid[r][c] == "1":
                    res += 1
                    stack.append((r, c))
        
                    while stack:
                        r_i, c_i = stack.pop()
                        if (
                            0 <= r_i < rows and 0 <= c_i < cols and
                            grid[r_i][c_i] == "1"
                        ):
                            # Consume and visit neighboring cells
                            grid[r_i][c_i] = "0"
                            for dr, dc in directions:
                                stack.append((r_i + dr, c_i + dc))
        return res 
