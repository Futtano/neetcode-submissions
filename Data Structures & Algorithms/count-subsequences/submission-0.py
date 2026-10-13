class Solution:
    # DFS 2D Dynamic programming
    # let m = len(s) and n = len(t)
    # Time: O(m*n)
    # Space: O(m*n)
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        cache = {}

        def dfs(i: int, j: int) -> int:
            # Completed t string
            if j == n:
                return 1
            # s string ended but not t
            # or there arent enough characters in s
            if i == m or (m-i) < (n-j):
                return 0
            if (i,j) in cache:
                return cache[(i, j)]

            count = 0
            # Current char does  match
            if s[i] == t[j]:
                count += dfs(i+1, j+1)
            # Try another subseq with next character
            count += dfs(i+1, j)

            cache[(i, j)] = count

            return count
            
        return dfs(0,0)