from collections import deque
from typing import List


class Solution:
    # Find safe nodes using Kahn's algorithm on the reversed graph.
    # Let V be the number of nodes and E the number of directed edges.
    # Time complexity: O(V + E)
    # Space complexity: O(V + E) auxiliary, plus O(V) for the output
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        predecessors = [[] for _ in range(n)]
        remaining = [len(neighbors) for neighbors in graph]

        # For each original edge node -> neighbor, record who points to neighbor.
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                predecessors[neighbor].append(node)

        # Terminal nodes have no outgoing edges and are safe immediately.
        queue = deque(node for node in range(n) if remaining[node] == 0)

        while queue:
            safe_node = queue.popleft()

            for predecessor in predecessors[safe_node]:
                # One more outgoing edge now leads to a confirmed safe node.
                remaining[predecessor] -= 1
                if remaining[predecessor] == 0:
                    queue.append(predecessor)

        # Scanning IDs in order gives the required ascending result.
        return [node for node in range(n) if remaining[node] == 0]