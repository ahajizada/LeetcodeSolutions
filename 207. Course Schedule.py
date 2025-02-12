class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)

        for course,pre in prerequisites:
            graph[pre].append(course)
        

        visited = set()
        rec_stack = set()

        def dfs(node):
            if node in rec_stack:
                return True
            
            if node in visited:
                return False
        

            visited.add(node)
            rec_stack.add(node)

            for nei in graph[node]:
                if dfs(nei):
                    return True
            
            rec_stack.remove(node)
            return False
        

        for course in range(numCourses):
            if dfs(course):
                return False
        
        return True
