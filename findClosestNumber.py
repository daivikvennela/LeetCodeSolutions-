class Solution(object):  
    userList = input(list)
    print(findClosestNumber(userList))
    def findClosestNumber(nums):  
        closest = nums[0]
        n = len(nums)
        # go through the array and use the concept of absolute value to find the number with the shortest distance to zero
        for i in range(n): 
            if (abs(nums[i])  < abs(closest)):
                closest = nums[i]

        if (closest < 0 and abs(closest) in nums):
            return abs(closest)
        else:
            return closest   
        