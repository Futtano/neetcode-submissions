class Solution:
    # Two pointers + sorting
    # Time: O(n log n)
    # Space: O(n) for Python's sorting; O(1) for the scan.
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0

        # If the heaviest cannot share with the lightest, they must go alone.
        # Otherwise, an optimal arrangement can be rearranged to pair them
        # without adding a boat.
        while left <= right:
            if left == right:
                # One person remains: they need one boat.
                boats += 1
                break

            if people[left] + people[right] <= limit:
                left += 1  # The lightest shares this boat.

            right -= 1  # The heaviest always leaves.
            boats += 1

        return boats