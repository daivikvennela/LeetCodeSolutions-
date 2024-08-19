class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        hash = {}
        counter = 0

        for i in range(len(jewels)):
            hash[jewels[i]] = i 

        for j in range(len(stones)):
            if stones[j] in hash:
                counter += 1
        
        return counter