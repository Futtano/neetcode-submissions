"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # Clone a graph using DFS and a map from originals to copies.
    # Let V be the number of nodes and E be the number of edges.
    # Time complexity: O(V + E)
    # Space complexity: O(V) auxiliary, plus O(V + E) for the output
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        clones = {}

        def clone(original: "Node") -> "Node":
            if original in clones:
                return clones[original]

            copy = Node(original.val)

            # Register the copy before exploring neighbors so that
            # an edge back to this node can reuse the same object.
            clones[original] = copy
            copy.neighbors = [clone(neighbor) for neighbor in original.neighbors]
            return copy

        return clone(node)