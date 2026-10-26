class Solution:
    # Iterative BFS with an explicit queue
    # Time O(r*c)
    # Space O(r*c) 
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # Possible movements from a cell
        directions = ((-1, 0), (1, 0), (0 ,-1), (0, 1))
        res = 0

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                # Found a new island
                if grid[r][c] == "1":
                    res += 1 # Update result
                    grid[r][c] = "0" # Mark as visited
                    queue.append((r, c)) # push into processing queue
                    while queue:
                        r_i, c_i = queue.popleft() 
                        for dr, dc in directions: # insert neighboring cells
                            nr, nc = r_i + dr, c_i + dc
                            if(
                                0 <= nr < rows and 0 <= nc < cols 
                                and grid[nr][nc] == "1"
                            ): # if they are ones, consume and append to processing queue
                                grid[nr][nc] = "0"
                                queue.append((nr, nc))
                        
        return res 
