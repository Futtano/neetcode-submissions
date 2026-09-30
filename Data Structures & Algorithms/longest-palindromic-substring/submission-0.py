class Solution:
    # Dynamic Programming
    # Time: O(n^2)
    # Space: O(n^2)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        best_start, best_len = 0, 1

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and (length <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if length > best_len:
                        best_start, best_len = i, length

        return s[best_start:best_start + best_len]