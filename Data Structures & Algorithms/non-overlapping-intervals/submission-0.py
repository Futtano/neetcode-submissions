class Solution:
    # Time: O(nlogn)
    # Space: O(n) (due to sorting)
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removed = 0

        end = intervals[0][1]

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            # remove the interval ending later;
            # keep the one ending earlier.
            if s < end:
                removed += 1
                end = min(end, e)
            else: # interval starts in [end,+infinity)
                # extend end 
                # (note: even if s does not
                #  start at *end*, because we
                #  sorted intervals we will not 
                #  encounter anything starting 
                # in (end, s] 
                end = e
        
        return removed
