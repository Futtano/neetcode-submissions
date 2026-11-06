class MedianFinder:
    # Find the running median with two balanced heaps
    # Let n be the number of values inserted so far.
    # Time complexity: O(log n) for addNum, O(1) for findMedian
    # Space complexity: O(n)
    def __init__(self):
        # Store the lower half as negated values and the upper half as-is.
        # Every value in the lower half is <= every value in the upper half.
        self.maxHeap = []
        self.minHeap = []
        self.size = 0

    def _rebalance(self) -> None:
        lowSize, hiSize = len(self.maxHeap), len(self.minHeap)

        # The lower heap must have either the same size or one extra value.
        if 0 <= lowSize - hiSize <= 1:
            return

        # A single insertion can create an imbalance that one transfer fixes.
        # Move the larger heap's root, which is the value at the boundary.
        src, dest = self.maxHeap, self.minHeap
        if hiSize > lowSize:
            src, dest = dest, src

        # The two heaps use opposite sign conventions.
        heapq.heappush(dest, -heapq.heappop(src))

    def addNum(self, num: int) -> None:
        # Compare with the largest value in the lower half.
        # The first value goes directly into the lower heap.
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        self._rebalance()
        self.size += 1

    def findMedian(self) -> float:
        # For an even count, the two roots are the two middle values.
        if self.size % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2

        # For an odd count, the lower heap holds the middle value at its root.
        return -self.maxHeap[0]