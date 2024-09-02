class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # to find the longest common prefix simply loop through and compare the letters of the other strings to the letter of the corresponding index in the first string

        # we need to to first find the min length so we dont get an out of bounds error
        # we do this by using a simple for loop tht stores the value of the lowest string length in the var minLen

        minLen = float('inf')
        for s in strs:
            if len(s) < minLen:
                minLen = len(s)
        i = 0 

        # this loop goes through the list of strings and checks if the letters at the index i are NOT equal to each other and if they are NOT equal i is incremented. As soon as the letter at the index i does not equal the letter the first string is returned all the way up to the index i 
        while i < minLen:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1

        return strs[0][:i]