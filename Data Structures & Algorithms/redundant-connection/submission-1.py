class Solution:
    # Union-Find with union by size and path halving.
    # Let n be the number of nodes, also equal to the number of edges.
    # Time complexity: O(n * alpha(n)) amortized over all operations
    # Space complexity: O(n) auxiliary
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(node: int) -> int:
            while node != parent[node]:
                # Point to the grandparent to shorten future searches.
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for u, v in edges:
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return [u, v]

            if size[root_u] < size[root_v]:
                root_u, root_v = root_v, root_u

            parent[root_v] = root_u
            size[root_u] += size[root_v]