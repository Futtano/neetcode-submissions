class Solution:
    # Time: O(n)
    # Space: O(n) at worst for temporary references during slice replacement
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals):
            el = intervals[i]

            # Non overlapping strictly lower
            if newInterval[1] < el[0]:
                intervals.insert(i, newInterval)
                return intervals

            # Non overlapping strictly greater
            if newInterval[0] > el[1]:
                i += 1
                continue

           # Merge
            new_low = min(el[0], newInterval[0])
            new_hi = max(el[1], newInterval[1])

            j = i + 1
            while (
                j < len(intervals) and
                intervals[j][0] <= new_hi
            ):
                new_hi = max(new_hi, intervals[j][1])
                j += 1

            intervals[i:j] = [[new_low, new_hi]]
            return intervals
            

        # Append at last position
        intervals.append(newInterval)
        return intervals
