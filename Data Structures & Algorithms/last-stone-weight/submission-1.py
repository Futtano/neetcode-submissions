class Solution:
    # Without using the Python 3.14 heapq API
    # use a min_heap as max_heap by negating each element
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-stone for stone in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            heavier, heavy = heapq.heappop(neg_stones), heapq.heappop(neg_stones)
            if heavier - heavy < 0:
                heapq.heappush(neg_stones, heavier - heavy)

        return -neg_stones[0] if len(neg_stones) > 0 else 0