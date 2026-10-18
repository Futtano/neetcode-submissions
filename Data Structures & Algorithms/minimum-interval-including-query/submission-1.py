class Solution:
    # let m = len(intervals) and n = len(queries)
    # Time: O(mlogm + nlogn)
    # Space: O(m + n)
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = []
        answers = {}
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(heap, (end - start +1, end))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            answers[q] = heap[0][0] if heap else -1

        return [answers[q] for q in queries]
        
                


