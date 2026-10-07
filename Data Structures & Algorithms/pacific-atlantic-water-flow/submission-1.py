class Solution:
    # BFS, inefficient
    # Time: O((n*m)^2)
    # Space: O(n*m)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        res = []

        def isPacific(x: int, y: int) -> bool:
            return x < 0 or y < 0

        def isAtlantic(x: int, y: int) -> bool:
            return y >= rows or x >= cols

        def flowsToBoth(x_c: int, y_c: int) -> bool:
            toAtlantic = False # whether we reached Atlantic
            toPacific = False # whether we reached Pacific
            queue = deque([(x_c, y_c)])
            visited = {(x_c, y_c)}
            
            while queue:
                # While there are element to process
                x, y = queue.popleft()
                for dx, dy in directions:
                    # Search all directions     
                    nx, ny = x + dx, y + dy
                    
                    # Update when we reach the two oceans
                    toAtlantic = toAtlantic or isAtlantic(nx, ny)
                    toPacific = toPacific or isPacific(nx, ny)

                    # We reached both, return True
                    if toAtlantic and toPacific:
                        return True
                    
                    # Negative height gradient, water propagates
                    # add to the processing queue
                    if (
                         0 <= nx < cols
                        and 0 <= ny < rows
                        and (nx, ny) not in visited
                        and heights[ny][nx] <= heights[y][x]
                    ):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return False

        for y in range(rows):
            for x in range(cols):
                if flowsToBoth(x, y):
                    res.append([y, x])

        return res