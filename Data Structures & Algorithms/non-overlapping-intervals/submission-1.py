class Solution:
    # Minimize removals by keeping the earliest-finishing intervals.
    # Let n = len(intervals).
    # Time complexity: O(n log n) for sorting, followed by an O(n) scan
    # Space complexity: O(n) for Python's sort, O(1) for the scan
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])

        last_end = float("-inf")
        removed = 0

        for start, end in intervals:
            if start < last_end:
                # The last kept interval ends no later than this one.
                # Remove the current interval and preserve last_end.
                removed += 1
            else:
                # This interval can follow the last kept one.
                last_end = end

        return removed