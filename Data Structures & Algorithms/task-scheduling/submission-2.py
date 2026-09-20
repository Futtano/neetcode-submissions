class Solution:
    # Time: O(T log 26) = O(T)
    # Space: O(26) = O(1)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-freq for freq in Counter(tasks).values()]
        heapq.heapify(heap)

        time = 0

        while heap:
            used = []

            # Process at most n + 1 different tasks in this cycle
            for _ in range(n + 1):
                if heap:
                    freq = heapq.heappop(heap) + 1

                    if freq < 0:
                        used.append(freq)

                    time += 1
                elif used:
                    # Idle slot needed because tasks are cooling down
                    time += 1
                else:
                    break

            for freq in used:
                heapq.heappush(heap, freq)

        return time