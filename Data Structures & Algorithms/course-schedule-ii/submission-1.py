from collections import defaultdict, deque
from typing import List


class Solution:
    # Build a topological ordering using Kahn's algorithm.
    # Let V = numCourses and E = len(prerequisites).
    # Time complexity: O(V + E)
    # Space complexity: O(V + E), including the O(V) order list
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        dependents = defaultdict(list)

        for course, prerequisite in prerequisites:
            # Finishing the prerequisite helps unlock the course.
            dependents[prerequisite].append(course)
            in_degree[course] += 1

        # Include every course that can be taken immediately.
        queue = deque(
            course for course in range(numCourses) if in_degree[course] == 0
        )
        order = []

        while queue:
            course = queue.popleft()
            # All prerequisites of this course already appear in order.
            order.append(course)

            for dependent in dependents[course]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)

        # Return an order only if it contains every course.
        return order if len(order) == numCourses else []