class Node:
    """Node of a double-linked list, storing a key and a value"""
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:
    """Cache of defined capacity, with a Least Recently Used eviction policy"""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache : dict[int, Node] = {}

        # left.next points to LRU node, right.next to the most recent
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def _remove(self, node: Node) -> None:
        """Remove a node from the double-linked list"""
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def _insert(self, node: Node) -> None:
        """Add a node to the double-linked list, before self.right"""
        prev, next = self.right.prev, self.right
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next 

    def get(self, key: int) -> int:
        """Get a value from the cache given its key. If the value is not present, return -1"""
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Remove the node from the list and add it again
        # So it is now the most recent access
        self._remove(node)
        self._insert(node)

        return node.val
        
    def put(self, key: int, value: int) -> None:
        """Put a value in the cache to be accessed with its key"""

        # If the key is alredy present in the cache, remove the
        # old entry
        if key in self.cache:
            self._remove(self.cache[key])

        # Create the new entry, add it to the cache and to the
        # double-linked list
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        # If we exceed the capacity, remove the LRU node
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]