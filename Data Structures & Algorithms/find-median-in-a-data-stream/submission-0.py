class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.minHeap and not self.maxHeap:
            # first item, just append it to maxHeap
            self.maxHeap.append(-num)
            return
        if self.maxHeap and not self.minHeap:
            # second item, append it to minHeap
            self.minHeap.append(num)

            # if the element in maxHeap is greater than the
            # element in minHeap switch the two heaps
            if -self.maxHeap[0] > self.minHeap[0]:
                self.maxHeap[0], self.minHeap[0] = -self.minHeap[0], -self.maxHeap[0]
            return

        # Main logic:
        
        # Add to maxHeap
        if num <= -self.maxHeap[0] or num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        elif num >= self.minHeap[0] or num > -self.maxHeap[0]: # add to minHeap
            heapq.heappush(self.minHeap, num)

        # Rebalance
        longest = self.minHeap if len(self.minHeap) > len(self.maxHeap) else self.maxHeap
        shortest = self.minHeap if len(self.minHeap) < len(self.maxHeap) else self.maxHeap
        while len(longest) - len(shortest) > 1:
            el = heapq.heappop(longest)
            heapq.heappush(shortest, -el)


    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + (-self.maxHeap[0])) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        return -self.maxHeap[0]
        
        