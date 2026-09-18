class Solution:
    # Standard minHeap of size K solution
    # Time: O(nlog2k)
    # Space: O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for el in nums:
            if len(minHeap) < k:
               heapq.heappush(minHeap, el)
            elif el >= minHeap[0]:
                heapq.heapreplace(minHeap, el)
        return minHeap[0]