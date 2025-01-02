class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        combinations = {")":"(", "}":"{", "]":"["}
        stack = []

        for c in s:
            if c in combinations:
                if stack and stack[-1] == combinations[c]:
                    stack.pop()
                
                else:
                    return False
            
            else:
                stack.append(c)
        
        return True if not stack else False
