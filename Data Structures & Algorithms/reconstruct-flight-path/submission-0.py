class Solution:
    # Hierholzer's algorithm
    # Let E be the total number of edges (or flight tickets)
    # Time: O(ElogE)
    # Space: O(E)
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Construct adjacency list
        adj = defaultdict(list)
        for source, dest in tickets:
            adj[source].append(dest)

        # Sort each entry in DESCENDING
        # order so that we can efficiently
        # use pop() in O(1)
        for key in adj.keys():
            adj[key].sort(reverse=True)

        itinerary = []
        def dfs(place: str) -> None:
            while adj[place]:
                dest = adj[place].pop()
                dfs(dest)
            
            itinerary.append(place)

        dfs("JFK")
        return list(reversed(itinerary))