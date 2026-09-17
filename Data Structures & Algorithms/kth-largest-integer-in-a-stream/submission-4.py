class KthLargest:
    # Manual min-heap implementation
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.storage = []

        for num in nums:
            self.add(num)

    def getParent(self, i):
        return (i - 1) // 2

    def getLeftChild(self, i):
        return 2 * i + 1

    def getRightChild(self, i):
        return 2 * i + 2

    def _percolate(self, i):
        while True:
            left = self.getLeftChild(i)
            right = self.getRightChild(i)
            smallest = i

            if (
                left < len(self.storage)
                and self.storage[left] < self.storage[smallest]
            ):
                smallest = left

            if (
                right < len(self.storage)
                and self.storage[right] < self.storage[smallest]
            ):
                smallest = right

            if smallest == i:
                break

            self.storage[i], self.storage[smallest] = (
                self.storage[smallest],
                self.storage[i],
            )

            i = smallest

    def _push(self, val):
        self.storage.append(val)
        i = len(self.storage) - 1

        while i > 0:
            parent = self.getParent(i)

            if self.storage[parent] <= self.storage[i]:
                break

            self.storage[parent], self.storage[i] = (
                self.storage[i],
                self.storage[parent],
            )

            i = parent

    def add(self, val: int) -> int:
        if len(self.storage) < self.k:
            self._push(val)

        elif val > self.storage[0]:
            self.storage[0] = val
            self._percolate(0)

        return self.storage[0]