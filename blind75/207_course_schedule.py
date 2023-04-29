# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.


class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        prereq_lists = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_lists[course].append(prereq)
        visited = set()

        def explore(course):
            if course in visited:
                return False
            if not len(prereq_lists[course]):
                return True

            visited.add(course)

            for prereq in prereq_lists[course]:
                if not explore(prereq):
                    return False

            visited.remove(course)
            prereq_lists[course] = []
            return True

        for course in range(numCourses):
            if not explore(course):
                return False
        return True


solution = Solution()
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(solution.canFinish(numCourses, prerequisites))
