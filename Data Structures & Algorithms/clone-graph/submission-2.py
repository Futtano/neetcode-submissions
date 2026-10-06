"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # Optimal BFS approach via queue
    # Time: O(V + E) where V are vertices and E are edges
    # Space: O(V) auxiliary space
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current = queue.popleft()
            clone = clones[current]

            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                clone.neighbors.append(clones[neighbor])

        return clones[node]