class Solution:
    # Dijkstra with expanded state (node, flights_used)
    #
    # n = number of airports
    # m = number of directed flights
    # k = maximum intermediate stops
    #
    # Time: O(n + (k+1)*m*log(n + (k+1)*m))
    # Space: O(n + (k+1)*(n+m))
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, price in flights:
            adj[u].append((v, price))


        max_flights = k + 1

        dist = [
            [float("inf")] * (max_flights + 1)
            for _ in range(n)
        ]

        dist[src][0] = 0

        heap = [(0, src, 0)] # cost, node, flights

        while heap:
            cost, node, hops = heapq.heappop(heap)

            if node == dst:
                return cost

            if cost > dist[node][hops]:
                continue

            if hops == max_flights:
                continue

            for nei, price, in adj[node]:
                new_cost = price + cost
                new_hops = hops + 1

                if new_cost < dist[nei][new_hops]:
                    dist[nei][new_hops] = new_cost
                    heapq.heappush(heap, (new_cost, nei, new_hops))


        return -1