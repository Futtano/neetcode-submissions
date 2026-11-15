class Solution:
    # Dijkstra
    # Time complexity: O((V+E)logV)
    # Space complexity: O(V + E)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, dest, w in times:
            adj[src].append((dest, w))

        dists = {i : float("inf") for i in range(1, n+1)}

        dists[k] = 0
        prQueue = [(0, k)] # (cost, node)

        while prQueue:
            dist, node = heapq.heappop(prQueue)

            if dist > dists[node]:
                continue

            for neigh, addDist in adj[node]:
                newDist = dist + addDist
                if newDist < dists[neigh]:
                    dists[neigh] = newDist
                    heapq.heappush(prQueue, (newDist, neigh))

        res = max(dists.values())
        return res if res != float("inf") else -1
