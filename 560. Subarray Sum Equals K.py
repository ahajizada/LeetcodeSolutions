class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        prefixSum = {0:1}
        curSum = 0

        for num in nums:
            curSum += num
            diff = curSum - k
            res += prefixSum.get(diff,0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum,0)
        
        return res
