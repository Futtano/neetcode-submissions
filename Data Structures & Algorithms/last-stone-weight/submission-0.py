class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            heavier, heavy = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if heavier - heavy > 0:
                heapq.heappush_max(stones, heavier - heavy)

        return stones[0] if len(stones) > 0 else 0