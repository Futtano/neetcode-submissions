class Solution:
    # Time: O(n)
    # Space: O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            # If the current height of the element is greater than the
            # previous one in the stack, we add it to the stack as the previous
            # element can extend further
            if i == 0 or height >= stack[-1][1]:
                stack.append((i, height))
                continue

            # This is not the first element and it's height is lower than the top
            # of the stack.
            while len(stack) > 0:
                # Pop and calculate the area
                start, el = stack.pop()
                area = (i - start) * el
                max_area = max(max_area, area)
                # If we finished the elements in the stack
                # or the next item on top of the stack has an height
                # lower than the current one, we can continue iterating,
                # but first we insert the current item height with the index
                # of the previously popped item as the area of current element
                # can extend backwards until an element of lower height (which
                # is now at the top of the stack)
                if not stack or height > stack[-1][1]:
                    stack.append((start, height))
                    break

        # Finished iterating across the array, pop the remaining elements
        # that extend until the end and calculate their area
        end = len(heights)
        while len(stack) > 0:
            start, el = stack.pop()
            area = (end - start) * el
            max_area = max(max_area, area)

        return max_area