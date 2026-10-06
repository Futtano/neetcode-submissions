class Solution:
    # BFS
    # Time: O(n*m)
    # Space: O(n*m)
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 0:
                    # Found a treasure, add it to the queue
                    queue.append((x, y))

        # Now the queue contains all the treasures,
        # use BFS to move and update each INF cell with the distance
        # from the nearest treasure

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        distance = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                # for each element in this step
                # update with the actual distance
                x, y = queue.popleft()
                for d_x, d_y in directions:
                    # add new valid positions to the queue
                    nx, ny = x + d_x, y + d_y
                    if (
                        0 <= nx < cols and
                        0 <= ny < rows and
                        grid[ny][nx] == INF
                    ):
                        grid[ny][nx] = distance + 1
                        queue.append((nx, ny))
            distance += 1
        

       