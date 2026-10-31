class MinStack:
    # Stack augmented with a minimum value at each level
    # Let n be the number of elements currently stored.
    # Time complexity: O(1) amortized for push/pop; O(1) for top/getMin
    # Space complexity: O(n)
    def __init__(self):
        # Each entry stores (value, minimum at this level and below).
        self.storage = []

    def push(self, val: int) -> None:
        # The first value is its own minimum. Otherwise, compare it
        # with the minimum already stored at the top.
        new_min = (
            val if not self.storage
            else min(val, self.storage[-1][1])
        )
        self.storage.append((val, new_min))

    def pop(self) -> None:
        # Removing the top exposes the previous minimum automatically.
        # Duplicate minima work because every level has its own summary.
        self.storage.pop()

    def top(self) -> int:
        # Read the value component of the top entry.
        return self.storage[-1][0]

    def getMin(self) -> int:
        # The top summary covers every element currently in the stack.
        return self.storage[-1][1]