class Solution:
    # Time: O(nlogn)
    # Space: O(1) 
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        start, end = intervals[0][0], intervals[0][1]
        res = []

        for s, e in intervals[1:]:
            # Case for strict subintervals
            if start <= s <= e <= end:
                continue
            # Case for extend right end
            elif start <= s <= end < e:
                end = e 
            # New interval
            else:
                res.append([start, end])
                start, end = s, e

        # Append last interval
        res.append([start, end])
        return res