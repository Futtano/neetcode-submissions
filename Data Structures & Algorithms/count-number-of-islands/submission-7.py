class Solution:
    # Union-Find
    # O(rows × cols × α(rows × cols))
    # Space O(r*c) 
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        parents = [
            r * cols + c if grid[r][c] == "1" else -1
            for r in range(rows)
            for c in range(cols)
        ]
        sizes = [1 if el != -1 else 0 for el in parents]
        count = sum(sizes)

        # Finds root of the component i
        def find(i: int) -> int:
            if parents[i] == i:
                return i
            parents[i] = find(parents[i])
            return parents[i]

        # Merge components, returns True if successful
        # False if i and j are part of the same components
        def union(i: int, j: int) -> bool:
            root_i = find(i)
            root_j = find(j)

            # They are part of the same component
            if root_i == root_j:
                return False

            # Merge the smallest component to the larger one
            small, large = root_i, root_j
            if sizes[small] > sizes[large]:
                small, large = large, small

            parents[small] = large
            sizes[large] += sizes[small]
            return True

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue

                current = r * cols + c
                for nr, nc in ((r + 1, c), (r, c + 1)):
                    if nr < rows and nc < cols and grid[nr][nc] == "1":
                        if union(current, nr * cols + nc):
                            count -= 1

        return count

