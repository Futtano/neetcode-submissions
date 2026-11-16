class Solution:
    # Scan-based Prim on the implicit complete graph.
    # Let V = len(points).
    # Time complexity: Θ(V²) with constant-time dictionary lookups.
    # Space complexity: Θ(V) auxiliary.
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Points are distinct. Each key represents one unvisited vertex.
        best = {tuple(point): float("inf") for point in points}
        best[tuple(points[0])] = 0  # Start without paying for an edge.
        total = 0

        while best:
            # Select the cheapest connection from the tree to an outside point.
            point = min(best, key=best.__getitem__)
            total += best.pop(point)

            # Only the newly added point can improve the remaining costs.
            x, y = point
            for neighbor in best:
                nx, ny = neighbor
                weight = abs(x - nx) + abs(y - ny)
                if weight < best[neighbor]:
                    best[neighbor] = weight

        return total
