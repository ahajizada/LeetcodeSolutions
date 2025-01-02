class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                currSum = nums[i] + nums[l] + nums[r]

                if currSum == 0:
                    result.append([nums[i],nums[l],nums[r]])

                    l += 1
                    r -= 1

                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                
                elif currSum > 0:
                    r -= 1
                
                else:
                    l += 1
            

        return result
