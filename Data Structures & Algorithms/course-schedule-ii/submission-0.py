class Solution:
    # DFS
    # Let V = numCourses and E = len(prerequisites)
    # Time: O(V + E)
    # Space: O(V + E)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen = set() # courses discovered by DFS
        taken = set() # courses whose DFS has completed

        dependencies = {} # mapping between course and its dependencies
        ordered_courses = [] # result

        # build dependencies dict
        for a, b in prerequisites:
            if a not in dependencies:
                dependencies[a] = []
            dependencies[a].append(b)

        # try to take a course, return True if success
        def take(course: int) -> bool:
            # course was already seen in this DFS path but
            # not completed -> cycle
            if course in seen and not course in taken:
                return False
            # already completed course
            if course in taken:
                return True

            seen.add(course)
            prereq = dependencies.get(course, [])

            # take all dependencies, if one does not
            # succeed, return False
            for p in prereq:
                if not take(p):
                    return False
            
            # We took all the prerequisites,
            # mark the course as taken and append
            # to the result
            taken.add(course)
            ordered_courses.append(course)
            return True

        for c in range(numCourses):
            if not take(c):
                return []

        return ordered_courses