class Solution:
    # DFS implicit recursion approach
    # Time O(r*c)
    # Space O(r*c) (recursion stack)
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # Possible movements from a cell
        directions = ((-1, 0), (1, 0), (0 ,-1), (0, 1))
        res = 0

        def dfs(r: int, c: int) -> None:
            if (
                0 <= r < rows and 0 <= c < cols 
                and grid[r][c] == "1"
            ): 
                # mark as 0 to consume it
                grid[r][c] = "0"
                # search all directions for adjacent 1s
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                # Found an islands, update result
                # and consume it
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)

        return res 
