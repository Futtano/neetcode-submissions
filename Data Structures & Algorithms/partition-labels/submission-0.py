class Solution:
    # Optimal Greedy Approach
    # Time: O(n)
    # Space: O(26) = O(1)
    def partitionLabels(self, s: str) -> List[int]:
        last_indexes = {
            ch: i
            for i, ch in enumerate(s)
        }
        lengths = []

        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last_indexes[ch])
            length = end - start + 1
            if i == end:
                lengths.append(length)
                start = i+1

        return lengths