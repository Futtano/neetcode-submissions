class Solution:
    # Complicated solution
    # Time: O(3n) = O(n)
    # Space: O(1)
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for i in range(len(target)):
            found = False

            for j in range(len(triplets)):
                if (
                    triplets[j][i] == target[i]
                    and all(
                        triplets[j][k] <= target[k]
                        for k in range(len(target))
                    )
                ):
                    found = True
                    break

            if not found:
                return False

        return True