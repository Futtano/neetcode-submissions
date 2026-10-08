class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1,text2 = text2, text1

        cache = {}

        def dfs(idx1: str, idx2: int) -> int:
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            if (idx1, idx2) in cache:
                return cache[(idx1, idx2)]

            maxlen = dfs(idx1+1, idx2) # skip current character from text1
            for j in range(idx2, len(text2)): # include current character from text1
                if text1[idx1] == text2[j]:
                    maxlen = max(
                        maxlen, 1 + dfs(idx1+1, j+1)
                    )

            cache[(idx1, idx2)] = maxlen

            return maxlen

        return dfs(0,0)