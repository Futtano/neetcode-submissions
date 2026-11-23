class Solution:
    # Longest Common Subsequence using one-row bottom-up DP
    # Let n = len(text1) and m = len(text2).
    # Time complexity: O(n * m)
    # Space complexity: O(min(n, m))
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Use the shorter string for the columns.
        if len(text2) > len(text1):
            text1, text2 = text2, text1

        n, m = len(text1), len(text2)
        dp = [0] * (m + 1)

        for i in range(n - 1, -1, -1):
            # For the rightmost character, down-right is the empty suffix.
            diagonal = 0

            for j in range(m - 1, -1, -1):
                below = dp[j]  # Old row at column j.
                right = dp[j + 1]  # Already updated in the current row.

                if text1[i] == text2[j]:
                    dp[j] = 1 + diagonal
                else:
                    dp[j] = max(below, right)

                # After moving left to j - 1, old column j is down-right.
                diagonal = below

        return dp[0]