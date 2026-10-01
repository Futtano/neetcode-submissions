class Solution:
    # Time: O(n)
    # Space: O(n)
    def numDecodings(self, s: str) -> int:

        cache = [-1]*len(s)

        def ways(i: str) -> int:
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if cache[i] != -1:
                return cache[i]

            total = ways(i + 1)

            if i + 1 < len(s) and int(s[i: i+2]) <= 26:
                total += ways(i + 2)

            cache[i] = total 

            return total

        return ways(0) 