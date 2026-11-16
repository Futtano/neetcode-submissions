from typing import List

Point = tuple[int, int]


class Solution:
    # Kruskal with union by size and path compression.
    # Let V = len(points), with E = V * (V - 1) // 2 candidate edges.
    # Time complexity: O(V² log V) worst case.
    # Space complexity: Θ(V²) auxiliary.
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = {(x, y): (x, y) for x, y in points}
        sizes = {point: 1 for point in parent}

        def find(point: Point) -> Point:
            if point != parent[point]:
                parent[point] = find(parent[point])
            return parent[point]

        def union(a: Point, b: Point) -> bool:
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False  # Adding this edge would close a cycle.

            # Attach the smaller component to the larger one.
            if sizes[root_a] < sizes[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            sizes[root_a] += sizes[root_b]
            return True

        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                cost = abs(x2 - x1) + abs(y2 - y1)
                edges.append((cost, (x1, y1), (x2, y2)))

        edges.sort()  # Cost is first, so edges are processed by weight.
        merged = 0
        total = 0

        for cost, a, b in edges:
            if union(a, b):
                total += cost
                merged += 1
                if merged == n - 1:
                    break  # All points now belong to one component.

        return total