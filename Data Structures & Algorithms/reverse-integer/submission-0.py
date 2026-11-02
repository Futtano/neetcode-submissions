class Solution:
    # Reverse decimal digits using negative arithmetic and overflow checks
    # Let d be the number of decimal digits in x (at most 10).
    # Time complexity: O(d), hence O(1) for signed 32-bit input
    # Space complexity: O(1)
    def reverse(self, x: int) -> int:
        positive = x > 0

        # Keep x nonpositive: abs(-2**31) would exceed the allowed range.
        if positive:
            x = -x

        # Positive results may end in 7 at the boundary; negative ones in 8.
        last_digit_limit = -7 if positive else -8
        result = 0

        while x:
            # Extract a nonpositive digit and remove it, truncating toward zero.
            digit = x % -10
            x = -(x // -10)

            # Check BEFORE multiplying, so no intermediate value overflows.
            if result < -214_748_364 or (
                result == -214_748_364 and digit < last_digit_limit
            ):
                return 0

            result = result * 10 + digit

        # The accumulated result is nonpositive; restore the original sign.
        return -result if positive else result