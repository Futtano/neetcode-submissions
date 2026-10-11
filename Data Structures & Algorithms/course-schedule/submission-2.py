class Solution:
    # DFS Search
    # Let V = numCourses and E = len(prerequisites)
    # Time: O(V + E)
    # space: O(V + E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # courses whose DFS has started
        seen = set()
        # courses whose DFS has started and completed
        taken = set()
        # Maps each course to its prerequisites
        prereq_map = {} 

        # Build the prerequisites mapping
        for a, b in prerequisites:
            if a not in prereq_map:
                prereq_map[a] = []
            prereq_map[a].append(b)

        # Try to take a course
        def take(course: int) -> bool:
            # Revisited a course still 
            # in the current DFS path: cycle
            if course in seen and not course in taken:
                return False

            # Already completed course
            if course in taken:
                return True

            # Add to processed courses
            seen.add(course)
            # Get prerequisites
            prereq = prereq_map.get(course, [])

            # Try to take all prerequisites 
            prereq_taken = True
            for c in prereq:
                prereq_taken = prereq_taken and take(c)
            
            # If we didn't succeed return False
            if not prereq_taken:
                return False

            # We can take the course
            taken.add(course)
            return True
            

        for i in range(numCourses):
            # try to take all courses
            if not take(i):
                return False

        return True           