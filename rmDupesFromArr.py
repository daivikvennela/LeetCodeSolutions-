"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.



"""

class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        k = 0
        n = len(nums)
        for i in range(len(nums)-1):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    k += 1
                    
    
        return(k)

    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
            


