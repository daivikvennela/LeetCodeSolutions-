'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
'''

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Start j from i + 1 to avoid duplicates
                if nums[i] + nums[j] == target:
                    return i, j
                else:
                    return None 