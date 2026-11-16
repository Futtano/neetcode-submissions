class Solution:
    # Lazy-heap Prim on the implicit complete graph.
    # Let V = len(points).
    # Time complexity: O(V² log V) worst case.
    # Space complexity: O(V²) auxiliary in the worst case.
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        unvisited = {(x, y) for x, y in points}
        best = {point: float("inf") for point in unvisited}

        start = tuple(points[0])
        best[start] = 0
        heap = [(0, start)]  # Start the tree without paying for an edge.
        total = 0

        while unvisited:
            cost, point = heapq.heappop(heap)
            if point not in unvisited:
                continue  # An earlier entry already added this point.

            unvisited.remove(point)
            total += cost

            x, y = point
            for neighbor in unvisited:
                nx, ny = neighbor
                weight = abs(x - nx) + abs(y - ny)

                if weight < best[neighbor]:
                    best[neighbor] = weight
                    heapq.heappush(heap, (weight, neighbor))

        return total
