class Solution:
    # Bellman-Ford
    #
    # n = number of airports (nodes)
    # m = number of directed flights (edges)
    # k = maximum intermediate stops
    #
    # Time: O(k * (n + m))
    # Space: O(n)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        max_flights = k + 1

        for _ in range(max_flights):
            tmp = prices.copy()
            for u, v, cost in flights:
                if prices[u] == float("inf"):
                    continue

                if prices[u] + cost < tmp[v]:
                    tmp[v] = prices[u] + cost

            prices = tmp


        return -1 if prices[dst] == float("inf") else prices[dst] 