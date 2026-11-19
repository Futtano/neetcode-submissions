class Solution:
    # Binary search for the minimum feasible eating speed
    # Let n = len(piles) and M = max(piles).
    # Time complexity: O(n + n log M)
    # Space complexity: O(1) auxiliary
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # At speed max(piles), each pile takes exactly one hour.
        left, right = 1, max(piles)

        # The minimum feasible speed always lies in [left, right].
        while left < right:
            speed = left + (right - left) // 2

            # Round up per pile because each hour is spent on a single pile.
            hours = sum((pile + speed - 1) // speed for pile in piles)

            if hours > h:
                # This speed and every slower one take too long.
                left = speed + 1
            else:
                # This speed works and could be the minimum.
                right = speed

        return left
