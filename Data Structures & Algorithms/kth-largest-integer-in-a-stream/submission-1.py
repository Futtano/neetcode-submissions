class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [float('-inf')] * k
        for el in nums:
            heapq.heappushpop(self.heap, el)

    def add(self, val: int) -> int:
        heapq.heappushpop(self.heap, val)
        return self.heap[0]