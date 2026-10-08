class Solution:
    # Dynamic programming optimal solution
    # Time: O(n * m)
    # Space: O(n * m)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def dfs(i: str, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if text1[i] == text2[j]:
                cache[(i, j)] =  1 + dfs(i + 1, j + 1) # matched current character
                return cache[(i, j)]
            
            cache[(i, j)] = max(
                dfs(i+1, j), # skip current character from text1
                dfs(i, j+1) # skip current character from text2
            )

            return cache[(i,j)]
            


        return dfs(0,0)