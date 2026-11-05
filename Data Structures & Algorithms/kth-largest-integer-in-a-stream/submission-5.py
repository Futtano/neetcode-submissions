class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums.copy()
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
            return self.nums[0]

        if val <= self.nums[0]:
            return self.nums[0]
        
        self.nums[0] = val
        
        # The new value belongs in the top k. 
        # Replace the root and sift down.
        heapq.heapreplace(self.nums, val)
        return self.nums[0]
