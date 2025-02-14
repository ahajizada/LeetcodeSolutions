
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        unique_islands = set()
        
        def dfs(r, c, base_r, base_c, shape):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 0  
                shape.append((r - base_r, c - base_c)) 
                for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:  
                    dfs(r + dr, c + dc, base_r, base_c, shape)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    shape = []
                    dfs(r, c, r, c, shape)
                    unique_islands.add(tuple(shape))  

        return len(unique_islands)
