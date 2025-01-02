class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sett = set(nums)

        longest = 0

        for num in sett:
            if num-1 not in sett:
                length = 1

                while num + length in sett:
                    length += 1
                
                longest = max(longest,length)
        
        return longest
