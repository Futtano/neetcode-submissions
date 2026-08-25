class Solution:
    # Dynamic Programming
    # Time: O(n)
    # Space: O(1)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize result array with zeros
        res = [0] * len(temperatures)

        # Iterate from right to left
        right = len(temperatures) - 1
        left = -1

        for i in range(right, left, -1):
            # For each i, start searching at the immediate followin index j
            j = i + 1

            # While we are within the array bounds and the current temperature
            # at index j is lower than that at the index i for which we are
            # calculating the days
            while j <= right and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    # There are no greater temperatures, let j jump to the end of
                    # array and break 
                    j = right + 1
                    break
                # Jump to the following greater temperature index
                j += res[j]

            # If we break out the while loop either
            # - We are out of bounds (if we searched all positions from j+1 to end of the array
            #       or we encountered a 0 in the previous results), j is set to right +1 and there
            #       is no greater temperature for the index i -> we keep res[i] to the default value
            #       of 0 meaning 'no greater temperatures'
            # - We found temperatures[j] > temperatures[i], we are within bounds so we set
            #       res[i] = j - i
            if j <= right:
                res[i] = j - i

        return res            