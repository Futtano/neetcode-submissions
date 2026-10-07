class Solution:
    # BFS
    # Time: O(n*m)
    # Space: O(n*m)
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        pacificGroup = set()
        atlanticGroup = set()

        def bfs(x: int, y: int, group: set) -> None:
            if (x, y) in group:
                return
            queue = deque([(x, y)])
            group.add((x, y))
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # Reverse flow: move to equal or higher cells.
                    if (
                        0 <= nx < cols
                        and 0 <= ny < rows
                        and heights[ny][nx] >= heights[y][x]
                        and (nx, ny) not in group
                    ):
                        group.add((nx, ny))
                        queue.append((nx, ny))

        pacificBorder = (
            [(0, y) for y in range(rows)]
            + [(x, 0) for x in range(cols)]
        )
        for x, y in pacificBorder:
            bfs(x, y, group=pacificGroup)

        atlanticBorder = (
            [(cols - 1, y) for y in range(rows)]
            + [(x, rows - 1) for x in range(cols)]
        )
        for x, y in atlanticBorder:
            bfs(x, y, group=atlanticGroup)

        bothOceansGroup = pacificGroup & atlanticGroup
        return [
            [y, x]
            for y in range(rows)
            for x in range(cols)
            if (x, y) in bothOceansGroup
        ]
