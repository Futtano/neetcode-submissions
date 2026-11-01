class ListNode:
    # Doubly linked-list node
    # Time complexity: O(1) to create a node
    # Space complexity: O(1) per node
    def __init__(self, val=0, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev


class MyLinkedList:
    # Doubly linked list with head/tail sentinels and nearest-end lookup
    # Let n be the number of real nodes currently stored.
    # Time complexity:
    #   Initialization, addAtHead, addAtTail: O(1)
    #   get, addAtIndex, deleteAtIndex: O(n) worst case
    # Space complexity: O(n) storage; O(1) auxiliary space per operation

    def __init__(self):
        # Sentinels ensure every real node has both neighbors.
        # An empty list connects the two sentinels directly.
        self.dummyHead = ListNode()
        self.dummyTail = ListNode()
        self.dummyHead.nxt = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        self.size = 0

    def _seek(self, index: int) -> ListNode | None:
        # Internal lookup also permits sentinel positions:
        # index == -1 returns dummyHead; index == size returns dummyTail.
        if index < -1 or index > self.size:
            return None

        # Count link traversals starting from each sentinel.
        stepsFromHead = index + 1
        stepsFromTail = self.size - index

        if stepsFromHead <= stepsFromTail:
            cur = self.dummyHead
            for _ in range(stepsFromHead):
                cur = cur.nxt
        else:
            cur = self.dummyTail
            for _ in range(stepsFromTail):
                cur = cur.prev

        return cur

    def get(self, index: int) -> int:
        # Public reads must exclude both sentinel positions.
        if index < 0 or index >= self.size:
            return -1

        return self._seek(index).val

    def addAtHead(self, val: int) -> None:
        # Connect the new node to its neighbors before updating them.
        node = ListNode(
            val,
            nxt=self.dummyHead.nxt,
            prev=self.dummyHead
        )
        self.dummyHead.nxt.prev = node
        self.dummyHead.nxt = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        # Insert between the current last node and the tail sentinel.
        node = ListNode(
            val,
            nxt=self.dummyTail,
            prev=self.dummyTail.prev
        )
        self.dummyTail.prev.nxt = node
        self.dummyTail.prev = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # Insertion at size is valid and appends; larger indices are invalid.
        if index < 0 or index > self.size:
            return

        # Insert immediately before this successor.
        # At index == size, the successor is dummyTail.
        nodeAtIndex = self._seek(index)
        nodeBefore = nodeAtIndex.prev

        newNode = ListNode(
            val,
            nxt=nodeAtIndex,
            prev=nodeBefore
        )

        # Reconnect both neighbors to the new node.
        nodeBefore.nxt = newNode
        nodeAtIndex.prev = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # Only real nodes may be removed.
        if index < 0 or index >= self.size:
            return

        nodeAtIndex = self._seek(index)
        nodeBefore = nodeAtIndex.prev
        nodeAfter = nodeAtIndex.nxt

        # Bypass the node in both directions.
        # Sentinels handle first, last, and only-node removal uniformly.
        nodeBefore.nxt = nodeAfter
        nodeAfter.prev = nodeBefore
        self.size -= 1