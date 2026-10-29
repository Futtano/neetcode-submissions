class MyCircularQueue:
    # Time complexity: O(1) for each operation, O(k) for construction
    # Space complexity for storage: O(k) where k is 
    # the capacity of the queue
    def __init__(self, k: int):
      self._capacity = k # max items that can be stored in the queue
      self._size = 0 # items stored in the queue
      self._storage = [None] * self._capacity
      self._w = 0  # points to the next enqueue position
      self._r = 0  # points to the next dequeue position

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self._storage[self._w] = value
        self._size += 1
        self._w = (self._w + 1) % self._capacity
        
        return True 

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self._size -= 1
        self._r = (self._r + 1) % self._capacity
        return True 

    def Front(self) -> int:
        return -1 if self.isEmpty() else self._storage[self._r]

    def Rear(self) -> int:
        last = (self._w - 1) % self._capacity
        return -1 if self.isEmpty() else self._storage[last]

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self._capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()