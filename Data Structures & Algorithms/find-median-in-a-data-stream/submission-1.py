class MedianFinder:
    # Two heaps (clean solution)
    # Time: O(nlogn) because O(log(n/2)) insert for each item and we insert n times = nlog(n/2) = nlogn 
    # Space: O(n)
    def __init__(self):
        self.minHeap = []  # upper half
        self.maxHeap = []  # lower half, stored as negatives

    def addNum(self, num: int) -> None:
        # Put num into the correct half
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        # Rebalance
        if len(self.maxHeap) > len(self.minHeap) + 1:
            el = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, el)

        elif len(self.minHeap) > len(self.maxHeap) + 1:
            el = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -el)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2

        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]

        return self.minHeap[0]