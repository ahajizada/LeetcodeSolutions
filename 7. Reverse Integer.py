class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MIN = -2147483648  # -2^31
        MAX = 2147483647   # 2^31 - 1

        res = 0
        sign = 1 if x > 0 else -1  
        x = abs(x)  

        while x != 0:
            digit = x % 10  
            x = x // 10  

            
            if (res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10)):
                return 0
            
            res = (res * 10) + digit

        return res * sign  
