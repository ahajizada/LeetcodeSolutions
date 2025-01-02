class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        longest = 0
        sett = set()

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            
            window = (r-l) + 1
            longest = max(longest,window)
            sett.add(s[r])
        
        return longest
