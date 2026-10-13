class Solution:
    # DFS 2D dynamic programming
    # Let m = len(matrix) and n(len(matrix[0]))
    # Time: O(m*n)
    # Space: O(m*n)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        cache = {}
        directions = (
            (0, 1), (0, -1), (1, 0), (-1, 0)
        )

        def dfs(r: int, c: int) -> int:
            if (r, c) in cache:
                return cache[(r,c)]

            segment = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    matrix[nr][nc] > matrix[r][c]
                ):
                    segment = max(segment, 1 + dfs(nr, nc))
            
            cache[(r, c)] = segment
            return segment

        for r in range(rows):
            for c in range(cols):
                length = dfs(r, c)
                if length > res:
                    res = length

        return res
