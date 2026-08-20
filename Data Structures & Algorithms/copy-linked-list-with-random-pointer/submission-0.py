"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        node_map = {}
        cur = head
        while cur:
            node_map[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            # next pointer update
            node_map[cur].next = node_map[cur.next] if cur.next else None

            # random pointer update
            node_map[cur].random = node_map[cur.random] if cur.random else None
            cur = cur.next

        return node_map[head]

