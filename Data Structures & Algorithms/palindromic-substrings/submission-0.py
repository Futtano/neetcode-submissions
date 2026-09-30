class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        totPalindromes = 0
        dp = [
            [False] * n for _ in range(n)
        ]

        for length in range(1, n + 1):
            for i in range(n - length +1):
                j = i + length - 1

                if s[i] == s[j] and (
                    length <= 3 or dp[i+1][j-1]
                ):
                    totPalindromes += 1
                    dp[i][j] = True

        return totPalindromes