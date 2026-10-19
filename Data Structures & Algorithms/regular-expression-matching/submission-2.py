
class Solution:
    # Top-down DP
    # Time(n*m)
    # Space(n*m)
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        memo = {}

        def dp(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern exhausted: string must also be exhausted
            if j == m:
                return i == n

            # Does the current character match?
            first_match = (
                i < n and (s[i] == p[j] or p[j] == ".")
            )

            # Handle zero or more repetitions
            if j + 1 < m and p[j + 1] == "*":
                result = (
                    dp(i, j + 2) or
                    (first_match and dp(i + 1, j))
                )
            else:
                # Ordinary character or '.'
                result = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dp(0, 0)
