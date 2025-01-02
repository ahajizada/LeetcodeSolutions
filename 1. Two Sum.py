class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashmap:
                return [hashmap[diff],i]
            
            hashmap[nums[i]] = i
        return []
