# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not k:
            return [target.val]
        
        q = collections.deque([root])
        graph = collections.defaultdict(list)

        while q:
            node = q.popleft()

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)

                q.append(node.left)
            
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)

                q.append(node.right)
            
        
        q = collections.deque([(target,0)])
        res = []
        visited = set([target])

        while q:
            node, distance = q.popleft()

            if distance == k:
                res.append(node.val)
            
            else:
                for edge in graph[node]:
                    if edge not in visited:
                        q.append((edge,distance + 1))
                        visited.add(edge)
            
        
        return res
