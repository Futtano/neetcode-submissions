class Solution:
    # One-pass insertion and merging. Let n = len(intervals).
    # Time complexity: O(n).
    # Space complexity: O(1) auxiliary, excluding the O(n) output.
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        start, end = newInterval

        for lo, hi in intervals:
            if hi < start:
                # This interval belongs before the pending interval.
                result.append([lo, hi])
            elif lo > end:
                # Sorted starts guarantee the pending interval is complete.
                result.append([start, end])
                start, end = lo, hi
            else:
                # Inclusive endpoints make touching intervals overlap.
                start = min(start, lo)
                end = max(end, hi)

        result.append([start, end])
        return result