class Solution:
    # Time: (nlogn)
    # Space: O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort positions and speeds in decreasing order of position
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        # For each car, starting from the head of the queue
        for pos, spd in cars:
            # Calculate the time it will take
            time = (target - pos) / spd

            # If it is the first car in the queue or it will
            # take longer than the cars ahead (top of stack)
            # append it as a new car fleet
            if not stack or time > stack[-1]:
                stack.append(time)

        # return the total number of fleets
        return len(stack)