class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        cur = 0
        prev = 0
        res = 0
        cur_operation = "+"
        
        while i < len(s):
            cur_char = s[i]

            # Build current number
            if cur_char.isdigit():
                cur = cur * 10 + int(cur_char)
            
            # If current char is an operator or at the end of the string
            if cur_char in "+-*/" or i == len(s) - 1:
                if cur_operation == "+":
                    res += cur
                    prev = cur
                elif cur_operation == "-":
                    res -= cur
                    prev = -cur
                elif cur_operation == "*":
                    res -= prev
                    res += prev * cur
                    prev = prev * cur
                elif cur_operation == "/":
                    res -= prev
                    res += int(float(prev) / cur)  # Handle truncation toward zero
                    prev = int(float(prev) / cur)
                
                # Update current operation and reset cur
                cur_operation = cur_char
                cur = 0
            
            i += 1
        
        return res
