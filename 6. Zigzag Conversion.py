class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        res = ""

        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r,len(s),increment):
                res += s[i]
                # check if we are in one of the middle rows
                if (r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        
        return res
