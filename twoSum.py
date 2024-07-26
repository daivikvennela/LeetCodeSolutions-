'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
'''

class Solution(object):
    def twoSum(self, nums, target):
    
        seen = {}
        n = len(nums)
        #num:index
        for i in range(n):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i