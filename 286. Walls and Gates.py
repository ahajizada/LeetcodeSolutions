class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        rows,cols = len(rooms),len(rooms[0])

        seen = set()
        q = deque()

        def addRoom(r,c):
            if r < 0 or c <0 or r == rows or c == cols or (r,c) in seen or rooms[r][c] == -1:
                return
            
            seen.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    seen.add((r,c))
        
        dist = 0

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist

                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
        
            dist += 1
