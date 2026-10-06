"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        queue = deque()
        queue.append(node)
        node_map = {}

        while queue:
            el = queue.popleft()
            if el.val not in node_map:
                node_map[el.val] = Node(el.val)
            clone = node_map[el.val]
            for n in el.neighbors:
                if n.val not in node_map:
                    queue.append(n)
                    node_map[n.val] = Node(n.val) 
                clone_neigh = node_map[n.val]
                node_map[el.val].neighbors.append(clone_neigh)

        return node_map[1]