class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        min_length = float("inf")

        for word in strs:
            if len(word) < min_length:
                min_length = len(word)
        

        i = 0

        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            
            i+=1
        
        return strs[0][:min_length]
