class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)

        for course,pre in prerequisites:
            graph[pre].append(course)
        
        visited = set()
        rec_stack = set()
        topological_order = []

        def dfs(node):
            if node in rec_stack:
                return False
            
            if node in visited:
                return True
            
            visited.add(node)
            rec_stack.add(node)

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            rec_stack.remove(node)
            topological_order.append(node)
            return True
        

        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return []
        
        return topological_order[::-1]
