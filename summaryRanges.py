class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # you are given a nums array and asked to to return back the ranges in the list, start by creating a list object and then moving on to create a loop that runs while i is less than the lenght of the array minus one and then anothter while loop to update the start i to find the breaks. As soon as you find a break you should check for 2 condition, the first one is wheter a single number should be added and the next one s wheter the range of numbers from the start to the the index i should be added. 

        f = []
        i = 0 


        while i < len(nums):

            start = nums[i]

            while i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:
                i += 1
            if start != nums[i]:
                f.append(str(start) + "->" + str(nums[i]))
                
            else:
                f.append(str(nums[i]))
        
            i += 1

        return f