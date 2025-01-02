class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        x = m-1
        y = n-1

        for i in range(m+n-1,-1,-1):
            if x < 0:
                nums1[i] = nums2[y]
                y -= 1
            
            elif y < 0:
                break
            
            elif nums1[x] > nums2[y]:
                nums1[i] = nums1[x]
                x -= 1
            
            else:
                nums1[i] = nums2[y]
                y-= 1
