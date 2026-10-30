class Solution:
    # Dynamic programming recursion 
    # Time complexity: O(n)
    # Space complexity: O(n)
    def climbStairs(self, n: int) -> int:
        cache = [None] * (n + 1)

        def dp(t: int) -> int:
            if cache[t] is not None:
                # return cached result if present
                return cache[t]
            if 0 <= t <= 1:
                # base cases 0 and 1
                return 1 

            # We can jump from t-2 or t-1 to t
            # solve subproblems and cache result
            sub2 = dp(t-2)
            sub1 = dp(t-1)

            cache[t] = sub1 + sub2

            return cache[t]

        return dp(n)
