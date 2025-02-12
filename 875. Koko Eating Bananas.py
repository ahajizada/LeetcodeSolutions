from math import ceil

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def k_works(k):
            hours = 0
            for p in piles:
                hours += -(-p // k)
            return hours <= h
        
        l = 1
        r = max(piles)

        while l < r:
            k = (l + r) // 2
            if k_works(k):
                r = k
            else:
                l = k + 1
        
        return l
