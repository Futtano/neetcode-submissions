class Solution:
    # BFS over each node
    # Let v=n and e=len(edges)
    # Time: O(v+e)
    # Space: O(v+e)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Build graph with edges in
        # both directions
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        processed = set()
        count = 0

        for node in range(n):
            if node not in processed:
                processed.add(node)
                count += 1
                queue = deque([node])
                
                while queue:
                    a = queue.popleft()
                    for b in graph[a]:
                        if b not in processed:
                            processed.add(b)
                            queue.append(b)

        return count