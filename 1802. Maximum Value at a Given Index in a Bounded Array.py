class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def get_sum(value, length):
            if value > length:
                return (value * 2 - length + 1) * length // 2
            else:
                return (value * (value + 1)) // 2 + (length - value)

        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            left_sum = get_sum(mid - 1, index)  
            right_sum = get_sum(mid - 1, n - index - 1)  
            total = left_sum + right_sum + mid  

            if total > maxSum:
                right = mid - 1
            else:
                left = mid

        return left
