class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen = set()
        taken = set()
        prereq_map = {}
        for a, b in prerequisites:
            if a not in prereq_map:
                prereq_map[a] = []
            prereq_map[a].append(b)

        def take(course: int) -> bool:
            if course in seen and not course in taken:
                return False

            if course in taken:
                return True

            seen.add(course)
            prereq = prereq_map.get(course, [])

            prereq_taken = True
            for c in prereq:
                prereq_taken = prereq_taken and take(c)
            if not prereq_taken:
                return False
            taken.add(course)
            return True
            

        for i in range(numCourses):
            take(i)

        return seen == taken            