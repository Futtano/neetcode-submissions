class Solution:
    # Detect cycles in course prerequisites using Kahn's algorithm.
    # Let V = numCourses and E = len(prerequisites).
    # Time complexity: O(V + E)
    # Space complexity: O(V + E) auxiliary
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependents = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prerequisite in prerequisites:
            dependents[prerequisite].append(course)
            in_degree[course] += 1

        # Include every course with no prerequisites, even isolated courses.
        queue = deque(
            course for course in range(numCourses) if in_degree[course] == 0
        )
        finished = 0

        while queue:
            course = queue.popleft()
            finished += 1

            # Finishing this course removes one unmet prerequisite
            # from each course that depends on it.
            for dependent in dependents[course]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)

        # If any courses remain, a cycle blocks their completion.
        return finished == numCourses
