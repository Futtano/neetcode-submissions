class Solution:
    # Prim's Algorithm
    # Time: O((V+E)logE)
    # Space: O(V+E)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = {(x, y): float("inf") for x, y in points} 
        unvisited = set(tuple(point) for point in points)

        min_cost = 0

        pq = [(0, tuple(points[0]))]

        while pq:
            d, (x, y) = heapq.heappop(pq)

            if (x, y) not in unvisited:
                continue
            min_cost += d
            unvisited.remove((x, y))

            for x_i, y_i in points:
                dt = abs(x - x_i) + abs(y - y_i)

                if dt < dist[(x_i, y_i)]:
                    dist[(x_i, y_i)] = dt
                    heapq.heappush(pq, (dt, (x_i, y_i)))

        return min_cost