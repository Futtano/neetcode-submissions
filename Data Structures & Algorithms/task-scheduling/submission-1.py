class Solution:
    # Time: O(T log 26) = O(T)
    # Space: O(26) = O(1)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = [0] * 26

        for el in tasks:
            freqs[ord(el) - ord('A')] -= 1

        scheduler = [s for s in freqs if s < 0]
        heapq.heapify(scheduler)

        queue = deque()
        t = 0

        while queue or scheduler:
            if not scheduler and queue:
                t = queue[0][1]

            if queue and queue[0][1] <= t:
                el = queue.popleft()
                heapq.heappush(scheduler, el[0])

            to_process = heapq.heappop(scheduler)

            if to_process < -1:
                queue.append((to_process + 1, t + 1 + n))

            t += 1

        return t