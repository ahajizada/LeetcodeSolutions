class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binarySearch(nums,target,True)
        right = self.binarySearch(nums,target,False)
        return [left,right]
    
    def binarySearch(self,nums,target,leftBias):
        l = 0
        r = len(nums) - 1
        i = -1

        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] < target:
                l = mid + 1
            
            elif nums[mid] > target:
                r = mid - 1
            
            else:
                i = mid

                if leftBias:
                    r = mid - 1
                
                else:
                    l = mid + 1
        return i  

