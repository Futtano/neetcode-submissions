class Solution:
    # Standard Greedy solution
    # Time: O(3n) = O(n)
    # Space: O(1)
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        merge = [0, 0, 0]

        for triplet in triplets:
            if all(triplet[i] <= target[i] for i in range(3)):
                for i in range(3):
                    merge[i] = max(merge[i], triplet[i])

        return merge == target