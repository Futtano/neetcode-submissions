class Solution:
    # Modified Dijkstra
    # where n is a single dimension of a nxn square grid
    # Time: O(n^2 *log(n))
    # Space: O(n^2)
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float("inf")] * n for _ in range(n)]
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

        dist[0][0] = grid[0][0]
        heap = [(dist[0][0], 0, 0)] # min elevation, i, j

        while heap:
            dst, x, y = heapq.heappop(heap)

            # outdated duplicate
            if dst > dist[x][y]:
                continue    
            
            # finalized target cell, return
            if x == n-1 and y == n-1:
                return dist[x][y] 

            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    alt = max(dist[x][y], grid[nx][ny])
                    if alt < dist[nx][ny]:
                        dist[nx][ny] = alt
                        heapq.heappush(heap, (alt, nx, ny))

        return dist[n-1][n-1]

            