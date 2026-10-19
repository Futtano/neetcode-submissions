class Solution:
    # Inefficient
    # Let m = len(word1) and n = len(word2)
    # Time: O(m*n(m+n))
    # Space: O(m*n(m+n))
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(i: int, j: int, edits: int) -> int:
            if (i, j, edits) in cache:
                return cache[(i, j, edits)]

            if j >= len(word2) and i < len(word1):
                # delete the remaining charachters from word1
                return  edits + (len(word1) - i)
            if j < len(word2) and i >= len(word1):
                # add remaining characters to word1
                return edits + (len(word2) - j) 

            if j == len(word2) and i == len(word1):
                return edits
            
            if word1[i] == word2[j]:
                cache[(i, j, edits)] = dfs(i+1, j+1, edits)
                return cache[(i, j, edits)]

            cache[(i, j, edits)] = min(
                dfs(i+1, j, edits+1), # delete
                dfs(i+1, j+1, edits+1), # replace
                dfs(i, j+1, edits+1) # insert
            )

            return cache[(i, j, edits)]

        return dfs(0,0,0)