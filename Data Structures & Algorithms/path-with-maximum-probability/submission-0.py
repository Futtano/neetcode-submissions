class Solution:
    # Find the most probable path using Dijkstra's algorithm.
    # Let V = n and E = len(edges).
    # Time complexity: O(V + (E + 1) * log(E + 2))
    # Space complexity: O(V + E) auxiliary
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adjacency = defaultdict(list)
        for (source, destination), probability in zip(edges, succProb):
            adjacency[source].append((destination, probability))
            adjacency[destination].append((source, probability))

        # Store negated probabilities so smaller keys represent better paths.
        best_neg_probability = [0.0] * n
        best_neg_probability[start_node] = -1.0
        heap = [(-1.0, start_node)]

        while heap:
            neg_probability, node = heapq.heappop(heap)

            # A smaller key for this node was discovered after this push.
            if neg_probability > best_neg_probability[node]:
                continue

            # Extending a path cannot improve its probability, so this pop
            # finalizes the destination's best probability.
            if node == end_node:
                return -neg_probability

            for neighbor, edge_probability in adjacency[node]:
                candidate = neg_probability * edge_probability
                if candidate < best_neg_probability[neighbor]:
                    best_neg_probability[neighbor] = candidate
                    heapq.heappush(heap, (candidate, neighbor))

        # No path with positive probability reaches the destination.
        return 0.0