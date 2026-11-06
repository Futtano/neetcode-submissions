class Solution:
    # Simulate stone smashes with an in-place max-heap
    # Let n = len(stones).
    # Time complexity: O(n log n)
    # Space complexity: O(1) auxiliary
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Negate each weight so the min-heap pops the heaviest stone first.
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)  # O(n) heap construction

        # Each round removes at least one stone overall.
        while len(stones) > 1:
            heaviest = -heapq.heappop(stones)
            second_heaviest = -heapq.heappop(stones)
            remaining = heaviest - second_heaviest

            # Equal weights destroy both stones.
            if remaining > 0:
                heapq.heappush(stones, -remaining)

        return -stones[0] if stones else 0


