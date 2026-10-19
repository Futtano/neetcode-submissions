class Solution:
    # Efficient
    # Let m = len(word1) and n = len(word2)
    # Time: O(m*n)
    # Space: O(m*n)
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i: int, j: int) -> int:
            if (i, j) in cache:
                return cache[(i, j)]

            if j == len(word2):
                return len(word1) - i

            if i == len(word1):
                return len(word2) - j

            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = 1 + min(
                    dfs(i + 1, j),      # delete
                    dfs(i + 1, j + 1),  # replace
                    dfs(i, j + 1)       # insert
                )

            return cache[(i, j)]

        return dfs(0, 0)