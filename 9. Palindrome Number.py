class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        num = x
        reverse = 0

        while (x > 0):
            lastdigit = x % 10
            reverse = reverse * 10 + lastdigit
            x = x // 10
        
        return True if reverse == num else False

         
