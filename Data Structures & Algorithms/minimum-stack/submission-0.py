class MinStack:
    # Rationale: push a tuple with the value and the current minimum
    # when getMin is called, return the minimum section of the tuple
    # for the item on the top
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        new_min = val if not self.data else min(val, self.getMin())
        self.data.append((val, new_min))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]
        
