class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start = sorted([i for i,j in intervals])
        end = sorted([j for i,j in intervals])

        res,count = 0,0
        s,e = 0,0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count +=1
            
            else:
                e += 1
                count -= 1

            res = max(res,count)
        
        return res
