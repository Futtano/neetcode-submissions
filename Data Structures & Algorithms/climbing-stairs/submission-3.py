class Solution:
    # Dynamic programming bottom-up iterative approach 
    # Time complexity: O(n)
    # Space complexity: O(1)
    def climbStairs(self, n: int) -> int:
        # Initial base cases, ways(0) and ways(1)
        # both equal to 1
        ways1 = ways2 = 1

        # One iteration -> one new state
        # loop from 2 to n+1 as ways(0) and
        # ways(1) are already computed
        for _ in range(2, n+1):
            # ways1 is ways(t-2)
            # ways2 is ways(t-1)
            # Compute ways(t)
            new_state = ways1 + ways2
            # ways(t-1) becomes ways(t-2)
            ways1 = ways2 
            # ways(t) becomes ways(t-1)
            ways2 = new_state

        # The last iteration result is in ways2
        return ways2