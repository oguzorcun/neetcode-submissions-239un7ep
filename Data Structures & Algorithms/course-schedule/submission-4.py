class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course_preq_map = [[] for _ in range(numCourses)]
        for course_preq in prerequisites:
            course_preq_map[course_preq[0]].append(course_preq[1])
        
        visited = set()
                
        def check_cycle(course: int, sub_visited: set) -> bool:
            if course in sub_visited: return True
            if course in visited: return False
            sub_visited.add(course)
            for preq in course_preq_map[course]:
                if check_cycle(preq, sub_visited):
                    return True
            visited.add(course)
            sub_visited.remove(course)
            return False

        for course in range(numCourses):
            sub_visited = set()
            if check_cycle(course, sub_visited):
                return False

        return True