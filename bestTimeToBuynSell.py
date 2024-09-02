class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Setting a minimum price
        minPrice = float('inf')
        maxProf = 0 

        # go through the prices and assign a minimum price
        # for each iteration calculate the curr profit and compare and adjust it to the max Prof. 
        for p in prices:
            if p < minPrice:
                minPrice = p 
            
            currProf = p - minPrice 
            if currProf > maxProf:
                maxProf = currProf
        
        return maxProf

            

            





        




                
            
        

            