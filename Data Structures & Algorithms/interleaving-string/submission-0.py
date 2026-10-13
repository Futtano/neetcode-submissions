class Solution:
    # DFS 2D dynamic programming
    # n = len(s1), m = len(s2)
    # Time: O(n*m)
    # Space: O(n*m)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Fundamental invariant
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        cache = {}

        def dfs(i: int, j: int) -> bool:
            if i + j == len(s3):
                return True
            if (i, j) in cache:
                return cache[(i,j)]
            

            k = i + j

            result = (
                i < n and s1[i] == s3[k] and dfs(i+1, j)
                or
                j < m and s2[j] == s3[k] and dfs(i, j+1)
            )

            
            cache[(i,j)] = result
            
            return result
       
        return dfs(0, 0)            