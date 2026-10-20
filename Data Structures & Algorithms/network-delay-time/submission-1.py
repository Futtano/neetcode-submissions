class Solution:
    # Dijkstra algorithm (lazy-insert version)
    # Time: O((V+E)logE)
    # Space: O(V + E)
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Construct adjaceny list and node set
        adj = defaultdict(list)
        nodes = set(range(1, n + 1))
        for v, u, w in times:
            adj[v].append((u, w))

        # Distances map
        dist = {v: float("inf") for v in nodes}
        # Start from k with distance 0
        dist[k] = 0
        hq = [(0, k)]

        while hq:
            d, node = heapq.heappop(hq)
            
            if node not in nodes:
                continue
            nodes.remove(node)

            for u, dt in adj[node]:
                alt = d + dt
                if alt < dist[u]:
                    heapq.heappush(hq, (alt, u))
                    dist[u] = alt
        
        return max(dist.values()) if not nodes else -1