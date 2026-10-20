class Solution:
    # Kruskal's Algorithm (Union-Find)
    # Time: O(E log E) = O(n^2 log n)
    # Space: O(V + E) = O(n^2)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        parent = list(range(n)) # component parents
        size = [1] * n # component sizes


        # Find the root of x's component (with path compression)
        def find(x: int) -> int:
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        # Merge two components using union by size.
# Return False if already connected (would create a cycle).
        def union(a: int, b: int) -> bool:
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False

            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]
            return True

        edges = []

        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                cost = abs(x2 - x1) + abs(y2 - y1)
                edges.append((cost, i, j))

        edges.sort()

        count = 0 # Number of edges accepted into the MST
        total = 0 # Total cost accumulated so far

        for cost, u, v in edges:
            if union(u, v): # if these are separated components we merge and update
                total += cost
                count += 1
                if count == n-1: # there are n-1 edges in a tree
                    break

        return total