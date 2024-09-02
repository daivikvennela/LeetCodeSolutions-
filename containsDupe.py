class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = set()
        # load into hashset and add if the value is not present if it is simply just return true
        for i in range(len(nums)):
            
            if nums[i] in n:
                return True
            else:
                n.add(nums[i])

        return False
        