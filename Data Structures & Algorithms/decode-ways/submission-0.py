from functools import cache

class Solution:
    # Time: O(n)
    # Space: O(n)
    def numDecodings(self, s: str) -> int:
        @cache
        def ways(i: str) -> int:
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            total = ways(i + 1)

            if i + 1 < len(s) and int(s[i: i+2]) <= 26:
                total += ways(i + 2)

            return total

        return ways(0) 