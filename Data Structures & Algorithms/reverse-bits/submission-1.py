class Solution:
    def reverseBits(self, n: int) -> int:
        # Time: O(1) (at most 32 iterations)
        # Space: O(1)
        res = 0
        exp = 31
        while n > 0:
            res += (1 << exp) * (n & 1)
            exp -=1
            n = n >> 1

        return res
