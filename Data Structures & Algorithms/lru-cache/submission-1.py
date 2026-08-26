class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache : dict[int, Node] = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def _insert(self, node: Node) -> None:
        prev, next = self.right.prev, self.right
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert(node)

        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            prev, next = lru.prev, lru.next
            prev.next, next.prev = next, prev
            del self.cache[lru.key]
