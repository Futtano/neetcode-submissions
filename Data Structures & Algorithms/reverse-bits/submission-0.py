class Solution:
    def reverseBits(self, n: int) -> int:
        # Time: O(n)
        # Space: O(1)
        res = 0
        exp = 31
        while n > 0:
            res += int((2**exp)) * (n & 1)
            exp -=1
            n = n >> 1

        return res
