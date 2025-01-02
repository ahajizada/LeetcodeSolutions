class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
  
        #Find Minimum Idx

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r-l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        minIdx = l

        if minIdx == 0:
            l = 0
            r = len(nums) - 1
        
        elif target >= nums[0] and target <= nums[minIdx - 1]:
            l = 0
            r = minIdx - 1
        
        else:
            l = minIdx
            r = len(nums) - 1
        
        while l <= r:
            mid = l + (r-l) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return -1

        
